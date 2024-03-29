import shutil
from logging import getLogger
from pathlib import Path

log = getLogger(__name__)

ARCHIVE_EXT = "zip"


class ComicArchiveUseCase:
    def __init__(self) -> None:
        pass

    def archive(self, path: str) -> None:
        vol_names = list(Path(path).iterdir())
        for vol_name in vol_names:
            log.info(f"{ARCHIVE_EXT} : root={path}, base={vol_name.name}")
            shutil.make_archive(vol_name.name, ARCHIVE_EXT, root_dir=path, base_dir=vol_name.name)
            shutil.move(vol_name.name + "." + ARCHIVE_EXT, path + "/")
