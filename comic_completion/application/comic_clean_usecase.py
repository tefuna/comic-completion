import os
from logging import getLogger
from pathlib import Path
from typing import List, Tuple

from domain.model.comic import Comic
from domain.model.id import Id
from domain.model.subid import Subid
from domain.model.volume import Volume

IS_RENAME_DRYRUN = "1"
RENAME_DRYRUN = os.environ["RENAME_DRYRUN"]
RENAME_DRYRUN_PATH = os.environ["RENAME_DRYRUN_PATH"]

log = getLogger(__name__)


class ComicCleanUseCase:
    def __init__(self) -> None:
        pass

    def validate(self, path: str) -> List[str]:
        # 読み込み：volumes
        comic_title = Comic.get_title_from_path(path)
        volumes: List[Volume] = []
        vol_names = list(Path(path).iterdir())
        if not vol_names:
            raise ValueError("no volume exist")
        for vol_name in vol_names:
            volume = Volume(vol_name.name, str(vol_name.resolve()), comic_title)
            volumes.append(volume)

        # 読み込み：comic
        comic = Comic(path, volumes)
        self.__comic = comic

        # 内容検証
        errors: List[str] = []
        for volume in volumes:
            errors.extend(volume.validate_name(comic.title))
            errors.extend(volume.validate_pages())
        return errors

    # =====================================================================
    # TODO リファクタリングしたい
    def rename_all(self, id: str) -> List[str]:
        # リネームファイルリスト作成
        id_o = Id(id)
        scale = len(str(len(self.__comic.volumes)))

        renames = []
        t = self.__comic.split_valid_volumes()
        for std_volume in t[0]:
            subid_o = Subid(str(std_volume.num), scale)
            vol_renames = self.__get_rename_tuple(std_volume, id_o, subid_o)
            renames.extend(vol_renames)

        # リネーム実行
        self.__rename_in(renames)

        # エラー巻タイトルのリターン
        errors: List[str] = []
        for bad_volume in t[1]:
            errors.append(bad_volume.name)
        return errors

    def rename_spec(self, vol_name: str, id: str, subid: str) -> None:
        id_o = Id(id)
        subid_o = Subid(subid, Subid.TYPE_STD)

        volume = self.__comic.get_volume_by_name(vol_name)
        renames = self.__get_rename_tuple(volume, id_o, subid_o)
        self.__rename_in(renames)

    def __get_rename_tuple(self, volume: Volume, id: Id, subid: Subid) -> List[Tuple]:
        renames = []
        page_num = 1
        for page in volume.pages:
            ext = Path(page).suffix
            name_src = f"{volume.path}\\{page}"
            name_dst = f"{volume.path}\\{id.value}-{subid.value}-{page_num:03}{ext}"
            renames.append((name_src, name_dst))
            page_num += 1
        return renames

    def __rename_in(self, renames: List[Tuple]) -> None:
        if RENAME_DRYRUN == IS_RENAME_DRYRUN:
            Path(RENAME_DRYRUN_PATH).parent.mkdir(parents=True, exist_ok=True)
            with open(RENAME_DRYRUN_PATH, mode="w", encoding='utf-8') as f:
                for rename_tup in renames:
                    f.write("\t".join(rename_tup) + "\n")
            log.info("rename with dryrun. please see dryrun result file.")
        else:
            for rename_tup in renames:
                os.rename(rename_tup[0], rename_tup[1])
