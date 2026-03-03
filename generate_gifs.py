from __future__ import annotations

import argparse
import os
import random
import sys
from pathlib import Path

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from maze.algorithms import available_algorithms, create_algorithm
from maze.grid import MazeGrid
from maze.image_renderer import render_grid_image


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate maze GIF animations")
    parser.add_argument(
        "--algo",
        default="all",
        help="Algorithm name or 'all'",
    )
    parser.add_argument("--width", type=int, default=20, help="Maze width (cells)")
    parser.add_argument("--height", type=int, default=12, help="Maze height (cells)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--cell-size", type=int, default=18, help="Cell size in pixels")
    parser.add_argument("--wall-width", type=int, default=2, help="Wall width in pixels")
    parser.add_argument("--frame-step", type=int, default=1, help="Capture one frame every N carvings")
    parser.add_argument("--duration", type=int, default=35, help="Frame duration in ms")
    parser.add_argument("--final-hold", type=int, default=700, help="Final frame hold in ms")
    parser.add_argument("--out-dir", default="outputs/gifs", help="Output directory")
    return parser


def resolve_algorithms(algo_arg: str) -> list[str]:
    names = available_algorithms()
    if algo_arg == "all":
        return names
    if algo_arg not in names:
        raise ValueError(
            f"Unsupported algorithm: {algo_arg}. Use one of {', '.join(names)} or 'all'."
        )
    return [algo_arg]


def generate_algorithm_gif(
    algo_name: str,
    width: int,
    height: int,
    seed: int,
    cell_size: int,
    wall_width: int,
    frame_step: int,
    duration: int,
    final_hold: int,
    out_dir: Path,
) -> Path:
    if frame_step <= 0:
        raise ValueError("frame_step must be positive")

    rnd = random.Random(seed)
    grid = MazeGrid(width=width, height=height)
    algorithm = create_algorithm(algo_name)

    frames = [
        render_grid_image(grid, cell_size=cell_size, wall_width=wall_width)
    ]

    def on_carve(_: int, __: int, ___: str) -> None:
        if grid.carve_count % frame_step == 0:
            frames.append(
                render_grid_image(grid, cell_size=cell_size, wall_width=wall_width)
            )

    grid.on_carve = on_carve
    algorithm.generate(grid, rnd)
    grid.on_carve = None

    if not frames:
        frames.append(render_grid_image(grid, cell_size=cell_size, wall_width=wall_width))

    frames.append(frames[-1].copy())

    out_dir.mkdir(parents=True, exist_ok=True)
    output_path = out_dir / f"{algo_name}_{width}x{height}_seed{seed}.gif"

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:-1] + [frames[-1]],
        duration=[duration] * (len(frames) - 1) + [final_hold],
        loop=0,
        optimize=False,
    )

    return output_path


def main() -> None:
    args = build_parser().parse_args()

    algorithm_names = resolve_algorithms(args.algo)
    out_dir = Path(args.out_dir)

    for algo_name in algorithm_names:
        output_path = generate_algorithm_gif(
            algo_name=algo_name,
            width=args.width,
            height=args.height,
            seed=args.seed,
            cell_size=args.cell_size,
            wall_width=args.wall_width,
            frame_step=args.frame_step,
            duration=args.duration,
            final_hold=args.final_hold,
            out_dir=out_dir,
        )
        print(f"[OK] {algo_name}: {output_path}")


if __name__ == "__main__":
    main()
