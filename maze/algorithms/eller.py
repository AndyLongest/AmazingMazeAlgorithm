from __future__ import annotations

import random

from maze.algorithms.base import MazeAlgorithm
from maze.grid import MazeGrid


class EllerAlgorithm(MazeAlgorithm):
    name = "eller"

    def generate(self, grid: MazeGrid, rnd: random.Random) -> None:
        next_set_id = 1
        current_row_sets = [0] * grid.width

        for y in range(grid.height):
            for x in range(grid.width):
                if current_row_sets[x] == 0:
                    current_row_sets[x] = next_set_id
                    next_set_id += 1

            for x in range(grid.width - 1):
                left = current_row_sets[x]
                right = current_row_sets[x + 1]

                if left == right:
                    continue

                should_join = y == grid.height - 1 or rnd.random() < 0.5
                if should_join:
                    grid.carve(x, y, "E")
                    old_set = right
                    new_set = left
                    for idx in range(grid.width):
                        if current_row_sets[idx] == old_set:
                            current_row_sets[idx] = new_set

            if y == grid.height - 1:
                continue

            next_row_sets = [0] * grid.width
            set_to_cells: dict[int, list[int]] = {}
            for x, set_id in enumerate(current_row_sets):
                set_to_cells.setdefault(set_id, []).append(x)

            for set_id, cells in set_to_cells.items():
                open_down_cells = [x for x in cells if rnd.random() < 0.5]
                if not open_down_cells:
                    open_down_cells = [rnd.choice(cells)]

                for x in open_down_cells:
                    grid.carve(x, y, "S")
                    next_row_sets[x] = set_id

            current_row_sets = next_row_sets
