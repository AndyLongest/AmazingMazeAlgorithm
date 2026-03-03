from __future__ import annotations

import random
from abc import ABC, abstractmethod

from maze.grid import MazeGrid


class MazeAlgorithm(ABC):
    name: str

    @abstractmethod
    def generate(self, grid: MazeGrid, rnd: random.Random) -> None:
        raise NotImplementedError
