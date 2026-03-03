import argparse
import os
import random
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from maze.grid import MazeGrid
from maze.renderers import render_ascii
from maze.algorithms import available_algorithms, create_algorithm


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Maze Algorithm Lab")
    parser.add_argument(
        "--algo",
        default="backtracker",
        choices=available_algorithms(),
        help="Algorithm name",
    )
    parser.add_argument("--width", type=int, default=20, help="Maze width (cells)")
    parser.add_argument("--height", type=int, default=10, help="Maze height (cells)")
    parser.add_argument("--seed", type=int, default=None, help="Random seed")
    return parser


def generate_maze(algo: str, width: int, height: int, seed: int | None) -> MazeGrid:
    rnd = random.Random(seed)
    grid = MazeGrid(width=width, height=height)

    algorithm = create_algorithm(algo)
    algorithm.generate(grid, rnd)

    return grid


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    grid = generate_maze(args.algo, args.width, args.height, args.seed)
    print(render_ascii(grid))


if __name__ == "__main__":
    main()
