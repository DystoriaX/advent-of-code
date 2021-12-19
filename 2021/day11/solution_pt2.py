from typing import List
import sys

GRID_SIZE = 10
REPETITION = 1_000_000

dr = [1, -1, 1, -1, 1, -1, 0, 0]
dc = [1, -1, -1, 1, 0, 0, 1, -1]


def explode(i, j, grid, flashed):
    flashed[i][j] = True
    grid[i][j] = 0

    for k in range(8):
        next_i = i + dr[k]
        next_j = j + dc[k]

        inside_boundary = 0 <= next_i < GRID_SIZE and 0 <= next_j < GRID_SIZE

        if not inside_boundary or flashed[next_i][next_j]:
            continue

        grid[next_i][next_j] += 1

        if grid[next_i][next_j] > 9:
            explode(next_i, next_j, grid, flashed)


def evolve(grid: List[List[int]]):
    flashed = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if flashed[i][j]:
                continue

            grid[i][j] += 1

            if grid[i][j] > 9:
                explode(i, j, grid, flashed)

    return all(all(row) for row in flashed)


if __name__ == "__main__":
    inp = sys.stdin.readlines()

    grid = [list(map(int, list(line.strip()))) for line in inp]

    ans = -1
    for step in range(REPETITION):
        if evolve(grid):
            ans = step + 1
            break

    print(ans)
