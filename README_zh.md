# 经典迷宫算法合集

[English](README.md) | 中文

本仓库收集与实现经典迷宫生成算法，并整理了不同算法的实现思路供学习。此外，本仓库使用统一网格模型和统一命令行入口，便于稳定地横向比较不同算法的行为和风格。

## 已收录算法

- Recursive Backtracker
- Randomized Prim
- Randomized Kruskal
- Aldous-Broder
- Sidewinder
- Eller

> 计划补充：Wilson、Binary Tree

## 仓库设计

- 统一数据结构：所有算法共享 `MazeGrid`
- 统一运行入口：通过 `main.py --algo` 切换算法
- 统一输出方式：ASCII 迷宫，便于快速比较结构差异
- 算法独立文件：`maze/algorithms/` 下每个算法一个 class

## 快速开始

环境要求：

- Python 3.10+

推荐初始化流程（从 GitHub 克隆后执行）：

```bash
python -m venv .venv
```

Windows PowerShell 激活虚拟环境：

```bash
.venv\Scripts\Activate.ps1
```

安装依赖：

```bash
python -m pip install -r requirements.txt
```

```bash
python main.py --algo backtracker --width 20 --height 10 --seed 42
```

查看当前可用算法：

```bash
python main.py --help
```

常用参数：

- `--algo`：算法名
- `--width`：迷宫宽（列）
- `--height`：迷宫高（行）
- `--seed`：随机种子（用于复现）

## 目录说明

- `main.py`：命令行入口与算法分发
- `maze/grid.py`：网格与墙体模型
- `maze/algorithms/`：算法实现目录（每个算法一个 class 文件）
- `maze/algorithms/base.py`：算法基类接口
- `maze/algorithms/__init__.py`：算法注册表与工厂
- `ROADMAP.md`：英文学习路线
- `ROADMAP_zh.md`：中文学习路线

## GIF 命令行指导

生成单个算法 GIF：

```bash
python generate_gifs.py --algo aldous --width 20 --height 12 --seed 42 --out-dir algorithm_gif
```

一次生成全部算法 GIF：

```bash
python generate_gifs.py --algo all --width 20 --height 12 --seed 42 --out-dir algorithm_gif
```

慢速教学版（更容易观察生成过程）：

```bash
python generate_gifs.py --algo all --width 12 --height 8 --seed 42 --frame-step 1 --duration 220 --final-hold 2500 --out-dir algorithm_gif
```

常用参数：

- `--frame-step`：每 N 次打墙录一帧（越大文件越小）
- `--duration`：每帧时长（毫秒）
- `--final-hold`：最后一帧停留时长（毫秒）
- `--out-dir`：输出目录

## 补充

仓库包含 GIF 演示与批量生成功能，可通过 `generate_gifs.py` 生成单个或全部算法动画。
