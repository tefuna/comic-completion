import os
import sys
from logging import config, getLogger

import yaml
from application.comic_clean_usecase import ComicCleanUseCase
from constant.constants import LOGGING_CONFIG
from dotenv import load_dotenv

load_dotenv()


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
    comic_clean_usecase = ComicCleanUseCase()
    errors = comic_clean_usecase.validate(path)
    if errors:
        log.error(f"invalid volumes or pages exists : {str(errors)}")
        return

    log.info("begin renaming page files")
    errors = comic_clean_usecase.rename_all(id)
    if errors:
        log.error(f"volumes that cannot rename exists : {str(errors)}")


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise ValueError(f"illegal arguments : {str(args)}")

    path = os.environ["BASE_DIR"] + "/" + args[1]
    id = args[2]
    main(path, id)
