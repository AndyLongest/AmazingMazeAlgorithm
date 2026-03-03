from __future__ import annotations

import random

from maze.algorithms.base import MazeAlgorithm
from maze.grid import MazeGrid


class SidewinderAlgorithm(MazeAlgorithm):
    name = "sidewinder"

    def generate(self, grid: MazeGrid, rnd: random.Random) -> None:
        for y in range(grid.height):
            run: list[int] = []
            for x in range(grid.width):
                run.append(x)

                at_eastern_boundary = x == grid.width - 1
                at_northern_boundary = y == 0

                should_close_out = at_eastern_boundary or (
                    not at_northern_boundary and rnd.random() < 0.5
                )

                if should_close_out:
                    if not at_northern_boundary:
                        carve_x = rnd.choice(run)
                        grid.carve(carve_x, y, "N")
                    run.clear()
                else:
                    grid.carve(x, y, "E")
