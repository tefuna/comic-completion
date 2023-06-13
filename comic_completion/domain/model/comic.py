import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Tuple

from domain.model.volume import Volume

REG_TITLE = re.compile(r"\] (.+) \[")
REG_VOL_COUNT = re.compile(r"\[完(\d+)\]")


@dataclass(frozen=True)
class Comic:
    path: str
    dirname: str = field(init=False)
    title: str = field(init=False)
    volumes: List[Volume] = field(default_factory=list)

    def __post_init__(self):
        # dirname
        object.__setattr__(self, "dirname", Path(self.path).name)

        # title
        title = REG_TITLE.findall(self.dirname)
        if len(title) != 1:
            raise ValueError(f"cannot find title from dirname : {self.dirname}")
        object.__setattr__(self, "title", title[0])

        # volume count
        vol_count = REG_VOL_COUNT.findall(self.dirname)
        if len(vol_count) != 1:
            raise ValueError(f"cannot find number of volumes : {self.title}")
        if int(vol_count[0]) > len(self.volumes):
            raise ValueError(f"insufficient volume : {self.title}")

    def split_valid_volumes(self) -> Tuple[List[Volume], List[Volume]]:
        vol_std = []
        vol_sub = []
        for volume in self.volumes:
            if volume.is_std_volume_name():
                vol_std.append(volume)
            else:
                vol_sub.append(volume)
        return (vol_std, vol_sub)

    # TODO Optionalにする
    def get_volume_by_name(self, volume_name) -> Volume:
        for volume in self.volumes:
            if volume.name == volume_name:
                return volume
        return None
