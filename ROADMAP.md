# Maze Algorithm Learning Roadmap

English | [中文](ROADMAP_zh.md)

## Learning goals

Using one shared grid model, implement multiple classic maze generation algorithms and understand:

- Core strategy of each algorithm
- Time/space trade-offs and implementation cost
- Maze style differences (corridor length, branch density, uniformity)

## Steps

### Step 1: Recursive Backtracker

- Core: depth-first expansion with stack-based backtracking
- Style: long corridors and strong directional feeling
- Complexity: time O(W×H), worst-case space O(W×H)
- Pitfall: unvisited-neighbor filtering and backtrack pop condition

Generation flow:

1. Pick a random start cell, mark visited, push into stack.
2. Check stack top and collect unvisited neighbors.
3. If any neighbor exists, randomly pick one, carve wall, mark visited, push it.
4. If none exists, pop stack (backtrack).
5. Repeat until stack is empty.

### Step 2: Randomized Prim

- Core: randomly grow from the frontier of the visited region
- Style: denser branching, shorter corridors
- Complexity: near O(W×H), frontier handling affects constants
- Pitfall: frontier duplicates and visited checks

Generation flow:

1. Pick a random start and mark visited.
2. Add edges from start to unvisited neighbors into frontier.
3. Randomly pick one frontier edge:
   - If target already visited, discard.
   - Otherwise carve and mark target visited.
4. Add new target's outgoing edges to unvisited neighbors into frontier.
5. Repeat until frontier is empty.

### Step 3: Randomized Kruskal

- Core: treat cells as disjoint sets, randomly remove walls between different sets
- Style: globally random, relatively balanced structure
- Complexity: about O(E α(V)), with E≈2WH-W-H on grid
- Pitfall: duplicate candidate walls and DSU correctness

Generation flow:

1. Initialize DSU with one set per cell.
2. Build candidate walls (typically east/south only) and shuffle.
3. For each wall, check roots of both sides:
   - Different roots: carve and union.
   - Same root: skip (avoid cycle).
4. Finish when all candidates are processed.

### Step 4: Wilson

- Core: loop-erased random walk (LERW)
- Style: produces a Uniform Spanning Tree (UST)
- Complexity: usually faster than Aldous-Broder, but more complex to implement
- Pitfall: loop-erasure order mistakes

Generation flow:

1. Put one random cell into the existing tree.
2. Start random walk from an unvisited cell and record path.
3. If walk loops into itself, erase the loop in path.
4. Stop when walk hits existing tree.
5. Carve full loop-erased path into tree.
6. Repeat until all cells are in tree.

### Step 5: Aldous-Broder

- Core: random walk; carve only when first visiting a cell
- Style: also gives UST; elegant but slow late phase
- Complexity: O(1) per step but high total walk steps (cover time)
- Pitfall: accidentally carving on revisits

Generation flow:

1. Pick random start as current and mark visited.
2. Move to a random neighbor each step.
3. If neighbor is first visit, carve current->neighbor and mark visited.
4. Set current = neighbor regardless.
5. End when all cells are visited.

### Step 6: Sidewinder / Binary Tree / Eller

- Sidewinder

  - Core: row-wise runs extending east, then one random north opening per run
  - Style: strong horizontal bias
  - Key: scan every row completely; close each run properly

  Generation flow:

  1. For each row, maintain a run while scanning left to right.
  2. Add current cell to run, decide extend-east or close-run.
  3. Extend-east: carve east.
  4. Close-run: pick one cell in run, carve north once, clear run.
  5. Force close at row end.
- Binary Tree

  - Core: each cell opens one of two fixed directions (e.g., north/east)
  - Style: simplest implementation, strongest directional bias
  - Key: useful baseline for style/performance comparison

  Generation flow:

  1. Define two candidate directions per cell.
  2. Choose one valid direction randomly.
  3. Carve and continue scan.
  4. End after full grid scan.
- Eller

  - Core: row-by-row set maintenance, horizontal merge + downward propagation
  - Style: stream-friendly generation, space O(W)
  - Key: at least one downward opening per set; force merge in last row

  Generation flow:

  1. Assign set IDs to cells without IDs in current row.
  2. Randomly merge adjacent different sets horizontally.
  3. For each set, carve south from one or more cells (at least one).
  4. Propagate those set IDs to next row; create new IDs for others.
  5. In final row, merge all remaining different sets.
