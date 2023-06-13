import os
import sys
from logging import config, getLogger

import yaml
from application.comic_clean_usecase import ComicCleanUseCase
from constant.constants import LOGGING_CONFIG

# logging
config.dictConfig(
    yaml.load(
        open(LOGGING_CONFIG, encoding="utf-8").read(),
        Loader=yaml.SafeLoader,
    )
)
log = getLogger(__name__)


def main(path: str, id: str) -> None:
    log.info("begin comic validation")
    comic_clean_usecase = ComicCleanUseCase(path)
    errors = comic_clean_usecase.validate()
    if errors:
        log.info(f"invalid volumes or pages exists : {str(errors)}")
        return

    log.info("begin renaming page files")
    errors = comic_clean_usecase.rename_all(id)
    if errors:
        log.info(f"volumes that cannot rename exists : {str(errors)}")


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise ValueError(f"illegal arguments : {str(args)}")

    path = os.environ["BASE_DIR"] + "/" + args[1]
    id = args[2]
    main(path, id)
