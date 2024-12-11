import re
from dataclasses import dataclass

REGEX = re.compile("[A-Z0-9_]{4}")


@dataclass(frozen=True)
class Id:
    value: str

    def __post_init__(self) -> None:
        if REGEX.match(self.value) is None:
            raise ValueError("invalid value: " + self.value)
