# snake-and-ladder-bfs
A Python-based Snake and Ladder mini project using the Breadth-First Search (BFS) algorithm to find the minimum number of dice throws required to reach the destination. 

# Snake and Ladder Using BFS

## Project Information
- Subject: Data Structures
- Course: SPPU SE Computer Engineering
- Language: Python
- Algorithm: Breadth-First Search (BFS)

## Abstract
This project implements the Snake and Ladder game using
the Breadth-First Search algorithm. The board is modeled
as a graph, where each cell represents a vertex and each
possible dice throw represents an edge.

BFS is used to determine the minimum number of dice throws
required to reach the final cell. Snakes move the player
backward, while ladders move the player forward.

## Objectives
- Understand graph representation and traversal.
- Implement BFS using a queue.
- Find the shortest path to the destination.
- Apply data structures to a real-world game problem.

## Data Structures Used
- Queue: Stores cells waiting to be explored.
- List: Stores visited cells and parent information.
- Dictionary: Stores snake and ladder positions.

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   python snake_ladder_bfs.py

## Algorithm
Breadth-First Search (BFS)

## Complexity Analysis
Time Complexity: O(N)
Space Complexity: O(N)

Here, N is the number of board cells. The board size
is fixed at 30 in this implementation.

## Conclusion
The project demonstrates how BFS can find the minimum
number of dice throws required to reach the destination
in a Snake and Ladder game by exploring the board
systematically.
