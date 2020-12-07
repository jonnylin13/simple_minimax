
'''

# Background
## Description
* Minimax algorithm - decision algorithm typically used in 2-player turn based games
* The goal of the algorithm is to find the most optimal move

## Concept
* There are two "agents" - one "minimizer" and one "maximizer"
* If we are able to evaluate each board state and assign a score, one agent tries to choose a board state with the highest score, and the other with the lowest

## Theory
* Based on zero-sum game theory, a gain on one side is a loss on the other -- "total utility is divided among players"
* Other examples being chess, poker, checkers, tic-tac-toe

# Implementation
## High-Level
* Goal is to find the best move for the player
* If we have a tree of branching decisions, we can choose the node with the best evaluation score
* To make the process better, we can also look ahead and evaluate potential opponent moves

## Cont'd
* Start with the root node
* Choose the best possible node

## How to evaluate
* The evaluation function can only assign scores to result nodes (leaves)
* Therefore, recursively reach leaves with scores and perform backpropagation

## Formal steps
1. Construct the game tree
2. Evaluate scores for each leaf using an evaluation function
3. Backpropagate scores from leaves to root, considering the player type (min/max)
4. At the root node, choose the node with max value and perform the corresponding move

# Documentation
TBD

