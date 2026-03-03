from __future__ import annotations

import random

from maze.algorithms.base import MazeAlgorithm
from maze.grid import MazeGrid


class _DisjointSet:
    def __init__(self) -> None:
        self.parent: dict[tuple[int, int], tuple[int, int]] = {}
        self.rank: dict[tuple[int, int], int] = {}

    def make_set(self, item: tuple[int, int]) -> None:
        self.parent[item] = item
        self.rank[item] = 0

    def find(self, item: tuple[int, int]) -> tuple[int, int]:
        root = item
        while self.parent[root] != root:
            root = self.parent[root]
        while item != root:
            parent = self.parent[item]
            self.parent[item] = root
            item = parent
        return root

    def union(self, a: tuple[int, int], b: tuple[int, int]) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False

        rank_a = self.rank[root_a]
        rank_b = self.rank[root_b]

        if rank_a < rank_b:
            self.parent[root_a] = root_b
        elif rank_b < rank_a:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1
        return True


class RandomizedKruskalAlgorithm(MazeAlgorithm):
    name = "kruskal"

    def generate(self, grid: MazeGrid, rnd: random.Random) -> None:
        dsu = _DisjointSet()
        for y in range(grid.height):
            for x in range(grid.width):
                dsu.make_set((x, y))

        edges: list[tuple[int, int, str]] = []
        for y in range(grid.height):
            for x in range(grid.width):
                if x + 1 < grid.width:
                    edges.append((x, y, "E"))
                if y + 1 < grid.height:
                    edges.append((x, y, "S"))

        rnd.shuffle(edges)

        for x, y, direction in edges:
            if direction == "E":
                nx, ny = x + 1, y
            else:
                nx, ny = x, y + 1

            if dsu.union((x, y), (nx, ny)):
                grid.carve(x, y, direction)
