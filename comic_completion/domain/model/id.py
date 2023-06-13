import re
from dataclasses import dataclass

REGEX = re.compile("[A-Z0-9]{4}")


@dataclass(frozen=True)
class Id:
    value: str

    def __post_init__(self):
        if REGEX.match(self.value) is None:
            raise ValueError("invalid value: " + self.value)
