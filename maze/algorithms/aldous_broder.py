from __future__ import annotations

import random

from maze.algorithms.base import MazeAlgorithm
from maze.grid import MazeGrid


class AldousBroderAlgorithm(MazeAlgorithm):
    name = "aldous"

    def generate(self, grid: MazeGrid, rnd: random.Random) -> None:
        current = (rnd.randrange(grid.width), rnd.randrange(grid.height))
        visited: set[tuple[int, int]] = {current}
        target_count = grid.width * grid.height

        while len(visited) < target_count:
            x, y = current
            direction, nx, ny = rnd.choice(grid.neighbors(x, y))

            if (nx, ny) not in visited:
                grid.carve(x, y, direction)
                visited.add((nx, ny))

            current = (nx, ny)
