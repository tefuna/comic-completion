import os
import re
from dataclasses import dataclass, field
from typing import List

NUM_NA = -1
REG_NUM = re.compile(r" 第(\d+)巻$")
REG_SUBTITLE = re.compile(r" (.+)$")
REG_VALID_EXT = re.compile(r"(.jpg|.jpeg|.png)$", flags=re.IGNORECASE)


@dataclass(frozen=True)
class Volume:
    name: str
    path: str
    num: int = field(init=False, default=NUM_NA)
    subtitle: str = field(init=False)
    pages: List[str] = field(default_factory=list)

    def __post_init__(self):
        # num
        num = REG_NUM.findall(self.name)
        if len(num) == 1:
            object.__setattr__(self, "num", int(num[0]))

        # subtitle
        subtitle = REG_SUBTITLE.findall(self.name)
        if not subtitle:
            raise ValueError("cannot get subtitle : " + self.name)
        object.__setattr__(self, "subtitle", subtitle[-1])

        # pages
        pages = sorted(os.listdir(self.path))
        if not pages:
            raise ValueError("cannot get subtitle : " + self.path)
        object.__setattr__(self, "pages", pages)

    def validate_name(self, title: str) -> List[str]:
        errors: List[str] = []
        if self.name.find(title) == -1:
            errors.append(title + ",-")
        return errors

    def validate_pages(self) -> List[str]:
        errors: List[str] = []
        for page in self.pages:
            if REG_VALID_EXT.search(page) is None:
                errors.append(self.name + "," + page)
        return errors

    def is_std_volume_name(self) -> bool:
        if self.num == NUM_NA:
            return False
        return True
