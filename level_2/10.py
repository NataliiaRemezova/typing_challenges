from constants import ___
from typing import TypeAlias


Coordinates: TypeAlias = tuple[int, int]


def is_point_in_square(point: Coordinates, left_upper_corner: Coordinates, right_bottom_corner: Coordinates) -> bool:
    pass


if __name__ == "__main__":
    assert is_point_in_square(
        point=(10, 12),
        left_upper_corner=(5, 5),
        right_bottom_corner=(20, 15)
    ) is True
