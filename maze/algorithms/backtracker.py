from __future__ import annotations

import random

from maze.algorithms.base import MazeAlgorithm
from maze.grid import MazeGrid


class RecursiveBacktrackerAlgorithm(MazeAlgorithm):
    name = "backtracker"

    def generate(self, grid: MazeGrid, rnd: random.Random) -> None:
        start_x = rnd.randrange(grid.width)
        start_y = rnd.randrange(grid.height)

        stack: list[tuple[int, int]] = [(start_x, start_y)]
        visited: set[tuple[int, int]] = {(start_x, start_y)}

        while stack:
            x, y = stack[-1]

            unvisited_neighbors = [
                (direction, nx, ny)
                for direction, nx, ny in grid.neighbors(x, y)
                if (nx, ny) not in visited
            ]

            if not unvisited_neighbors:
                stack.pop()
                continue

            direction, nx, ny = rnd.choice(unvisited_neighbors)
            grid.carve(x, y, direction)
            visited.add((nx, ny))
            stack.append((nx, ny))
