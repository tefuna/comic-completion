import shutil
from logging import getLogger
from pathlib import Path

log = getLogger(__name__)

ARCHIVE_EXT = "zip"


class ComicArchiveUseCase:
    def __init__(self, path: str):
        self.__path = path

    def archive(self) -> None:
        vol_names = list(Path(self.__path).iterdir())
        for vol_name in vol_names:
            log.info(f"{ARCHIVE_EXT} : root={self.__path}, base={vol_name.name}")
            shutil.make_archive(vol_name.name, "{ARCHIVE_EXT}", root_dir=self.__path, base_dir=vol_name.name)
            shutil.move(vol_name.name + "." + ARCHIVE_EXT, self.__path + "/")
