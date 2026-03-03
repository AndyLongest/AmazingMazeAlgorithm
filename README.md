# Maze Algorithm Collection

English | [中文](README_zh.md)

This repository focuses on collecting and implementing classic maze generation algorithms with one shared grid model and one CLI entry, so behavior and style can be compared consistently.

This repository also organizes implementation ideas for each algorithm to support learning and side-by-side comparison.

## Included algorithms

- Recursive Backtracker
- Randomized Prim
- Randomized Kruskal
- Aldous-Broder
- Sidewinder
- Eller

> Planned: Wilson, Binary Tree

## Repository design

- One shared data model: all algorithms use `MazeGrid`
- One runtime entry: switch algorithms via `main.py --algo`
- One output style: ASCII mazes for quick structural comparison
- One file per algorithm class in `maze/algorithms/`

## Quick start

Prerequisites:

- Python 3.10+

Recommended setup (from a fresh clone):

```bash
python -m venv .venv
```

Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

```bash
python main.py --algo backtracker --width 20 --height 10 --seed 42
```

Show available algorithms:

```bash
python main.py --help
```

Common arguments:

- `--algo`: algorithm name
- `--width`: maze width (columns)
- `--height`: maze height (rows)
- `--seed`: random seed for reproducibility

## Structure

- `main.py`: CLI entry and algorithm dispatch
- `maze/grid.py`: grid and wall model
- `maze/algorithms/`: algorithm classes (one class per file)
- `maze/algorithms/base.py`: algorithm base interface
- `maze/algorithms/__init__.py`: registry and factory
- `ROADMAP.md`: English learning roadmap
- `ROADMAP_zh.md`: Chinese learning roadmap

## GIF CLI Guide

Generate a GIF for one algorithm:

```bash
python generate_gifs.py --algo aldous --width 20 --height 12 --seed 42 --out-dir algorithm_gif
```

Generate GIFs for all algorithms:

```bash
python generate_gifs.py --algo all --width 20 --height 12 --seed 42 --out-dir algorithm_gif
```

Slow teaching mode (easier to follow generation steps):

```bash
python generate_gifs.py --algo all --width 12 --height 8 --seed 42 --frame-step 1 --duration 220 --final-hold 2500 --out-dir algorithm_gif
```

Common GIF arguments:

- `--frame-step`: capture one frame every N carve operations (larger means smaller file)
- `--duration`: per-frame duration in milliseconds
- `--final-hold`: final frame hold time in milliseconds
- `--out-dir`: output directory

## Note

The repository also includes GIF demo and batch generation support via `generate_gifs.py`.

