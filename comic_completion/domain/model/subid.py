from dataclasses import dataclass, field


@dataclass(frozen=True)
class Subid:
    TYPE_STD = -1

    value: str = field(init=False)
    seed: str
    scale: int

    def __post_init__(self):
        if self.scale == self.TYPE_STD:
            object.__setattr__(self, "value", self.seed)
        else:
            scale = self.scale if self.scale >= 2 else 2
            object.__setattr__(self, "value", self.seed.zfill(scale))
