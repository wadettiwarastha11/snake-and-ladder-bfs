
from collections import deque

BOARD_SIZE = 30

# Snakes and ladders
jumps = {
    3: 22,
    5: 8,
    11: 26,
    20: 29,
    17: 4,
    19: 7,
    21: 9,
    27: 1
}


def snake_and_ladder_bfs():
    queue = deque([(1, 0)])
    visited = [False] * (BOARD_SIZE + 1)
    parent = [-1] * (BOARD_SIZE + 1)

    visited[1] = True

    while queue:
        cell, throws = queue.popleft()

        if cell == BOARD_SIZE:
            path = []
            current = BOARD_SIZE

            while current != -1:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("Snake and Ladder using BFS")
            print("--------------------------------")
            print("Starting Cell: 1")
            print("Destination Cell:", BOARD_SIZE)
            print("Minimum Dice Throws:", throws)
            print("Shortest Path:", path)
            return

        for dice in range(1, 7):
            next_cell = cell + dice

            if next_cell > BOARD_SIZE:
                break

            destination = jumps.get(next_cell, next_cell)

            if not visited[destination]:
                visited[destination] = True
                parent[destination] = cell
                queue.append((destination, throws + 1))

    print("Destination cannot be reached.")


if __name__ == "__main__":
    snake_and_ladder_bfs()
