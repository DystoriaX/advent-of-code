import sys


# Helper list to traverse adjacent cells
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
count = 0


def find_flow(i, j, grid, vis):
    global count

    vis[i][j] = True
    count += 1
    HEIGHT = len(grid)
    WIDTH = len(grid[0])

    for k in range(4):
        next_i = i + dr[k]
        next_j = j + dc[k]

        is_valid = 0 <= next_i < HEIGHT and 0 <= next_j < WIDTH

        if (
            not is_valid
            or vis[next_i][next_j]
            or grid[i][j] >= grid[next_i][next_j]
            or grid[next_i][next_j] == "9"
        ):
            continue

        find_flow(next_i, next_j, grid, vis)


if __name__ == "__main__":
    inp = sys.stdin.readlines()

    grid = list(map(lambda x: x.strip(), inp))

    HEIGHT = len(grid)
    WIDTH = len(grid[0])

    risk_level = 0
    basins = []
    vis = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for i in range(HEIGHT):
        for j in range(WIDTH):
            is_lowest = True
            for k in range(4):
                next_i = i + dr[k]
                next_j = j + dc[k]

                is_valid = 0 <= next_i < HEIGHT and 0 <= next_j < WIDTH

                if not is_valid:
                    continue

                is_lowest = is_lowest and grid[i][j] < grid[next_i][next_j]

            if is_lowest:
                count = 0
                find_flow(i, j, grid, vis)
                basins.append(count)

    basins.sort(reverse=True)
    print(basins[0] * basins[1] * basins[2])
