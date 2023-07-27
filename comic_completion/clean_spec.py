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


def main(path: str, id: str, spec_vol_name: str, subid: str) -> None:
    log.info("begin comic validation")
    comic_clean_usecase = ComicCleanUseCase()
    errors = comic_clean_usecase.validate(path)
    if errors:
        log.warn(f"invalid volumes or pages exists : {str(errors)}")
        print("invalid volumes or pages exists, but continue process.  PRESS ANY KEY...")
        input()

    log.info("begin renaming page files of specified volume")
    comic_clean_usecase.rename_spec(spec_vol_name, id, subid)


if __name__ == "__main__":
    args = sys.argv
    if len(sys.argv) != 5:
        raise ValueError(f"illegal arguments : {str(args)}")

    path = os.environ["BASE_DIR"] + "/" + args[1]
    id = args[2]
    spec_vol_name = args[3]
    subid = args[4]
    main(path, id, spec_vol_name, subid)
