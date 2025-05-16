from dataclasses import dataclass


@dataclass(frozen=True)
class Price:
    value: float

    def __post_init__(self):
        if self.value <= 0:
            raise ValueError("Price must be positive")


@dataclass(frozen=True)
class Quantity:
    value: int

    def __post_init__(self):
        if self.value < 0:
            raise ValueError("Quantity must be non-negative")
