from __future__ import annotations

import random

from maze.algorithms.base import MazeAlgorithm
from maze.grid import MazeGrid


class RandomizedPrimAlgorithm(MazeAlgorithm):
    name = "prim"

    def generate(self, grid: MazeGrid, rnd: random.Random) -> None:
        start = (rnd.randrange(grid.width), rnd.randrange(grid.height))
        visited: set[tuple[int, int]] = {start}
        frontier: list[tuple[int, int, int, int, str]] = []

        sx, sy = start
        for direction, nx, ny in grid.neighbors(sx, sy):
            frontier.append((sx, sy, nx, ny, direction))

        while frontier:
            edge_index = rnd.randrange(len(frontier))
            x, y, nx, ny, direction = frontier.pop(edge_index)

            if (nx, ny) in visited:
                continue

            grid.carve(x, y, direction)
            visited.add((nx, ny))

            for n_direction, nnx, nny in grid.neighbors(nx, ny):
                if (nnx, nny) not in visited:
                    frontier.append((nx, ny, nnx, nny, n_direction))
