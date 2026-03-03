from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


DIRS = {
    "N": (0, -1),
    "S": (0, 1),
    "W": (-1, 0),
    "E": (1, 0),
}

OPPOSITE = {
    "N": "S",
    "S": "N",
    "W": "E",
    "E": "W",
}


@dataclass
class Cell:
    x: int
    y: int
    walls: dict[str, bool]


class MazeGrid:
    def __init__(self, width: int, height: int) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")

        self.width = width
        self.height = height
        self.carve_count = 0
        self.on_carve: Callable[[int, int, str], None] | None = None
        self._cells = [
            [
                Cell(x=x, y=y, walls={"N": True, "S": True, "W": True, "E": True})
                for x in range(width)
            ]
            for y in range(height)
        ]

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def cell(self, x: int, y: int) -> Cell:
        return self._cells[y][x]

    def neighbors(self, x: int, y: int) -> list[tuple[str, int, int]]:
        result: list[tuple[str, int, int]] = []
        for direction, (dx, dy) in DIRS.items():
            nx = x + dx
            ny = y + dy
            if self.in_bounds(nx, ny):
                result.append((direction, nx, ny))
        return result

    def carve(self, x: int, y: int, direction: str) -> None:
        dx, dy = DIRS[direction]
        nx = x + dx
        ny = y + dy

        if not self.in_bounds(nx, ny):
            raise ValueError("Cannot carve outside grid")

        self.cell(x, y).walls[direction] = False
        self.cell(nx, ny).walls[OPPOSITE[direction]] = False
        self.carve_count += 1

        if self.on_carve is not None:
            self.on_carve(x, y, direction)
