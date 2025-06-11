# Connect 4 Solvers

This project implements AI strategies for Connect4, utilizing Minimax and Alpha-Beta Pruning to determine the best possible move for a player in a given board state. Both algorithms search to a specified depth to evaluate the optimal action, helping the AI make informed decisions.

1. Minimax: A depth-first search algorithm that evaluates possible moves and selects the best one.
2. Alpha-Beta Pruning: An optimized version of Minimax that reduces unnecessary evaluations using alpha-beta bounds.

# Algorithms
## Minimax Algorithm: 
Minimax explores all possible game states up to a given depth (ply) and evaluates board positions. It maximizes score for X (the maximizing player), and minimizes score for O (the minimizing player). After doing so, it returns the optimal move and the total number of game nodes expanded.

## Alpha-Beta Pruning
Alpha-Beta pruning improves Minimax efficiency by cutting off branches that do not influence the final decision. It does so by using alpha (best option for maximizer) and beta (best option for minimizer) to prune the search tree.

# Run the Program
```python3 script.py```

# Demo

https://github.com/user-attachments/assets/29cce43a-9b0f-40ce-96e4-f2658dae05df


