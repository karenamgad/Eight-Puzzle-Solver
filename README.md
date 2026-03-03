# 8-Puzzle Solver

This repository contains a Python implementation of the **8-Puzzle problem solver** using multiple search algorithms.  
The program demonstrates classical AI search techniques applied to a sliding puzzle.

---

## Features

- **Breadth-First Search (BFS)**  
  Explores all possible moves level by level. Guarantees the shortest path solution.

- **Depth-First Search (DFS)**  
  Explores as deep as possible before backtracking. Memory efficient but may not find the shortest path.

- **Iterative Deepening DFS (IDFS)**  
  Combines the space efficiency of DFS and completeness of BFS.

- **A* Search**  
  Uses heuristics to find the optimal path faster:
  - **Manhattan distance**: sum of horizontal and vertical distances of tiles from goal positions.
  - **Euclidean distance**: straight-line distance from current tile to goal position.

- Visualizes the solution path and prints the sequence of moves.

---
