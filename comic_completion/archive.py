import os
import sys
from logging import config, getLogger

import yaml
from application.comic_archive_usecase import ComicArchiveUseCase
from constant.constants import LOGGING_CONFIG

# logging
config.dictConfig(
    yaml.load(
        open(LOGGING_CONFIG, encoding="utf-8").read(),
        Loader=yaml.SafeLoader,
    )
)
log = getLogger(__name__)


def main(path: str) -> None:
    comic_archive_usecase = ComicArchiveUseCase(path)
    log.info("begin archive process")
    comic_archive_usecase.archive()


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        raise ValueError(f"illegal arguments : {str(args)}")

    path = os.environ["BASE_DIR"] + "/" + args[1]
    main(path)
