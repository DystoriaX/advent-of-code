import sys

if __name__ == "__main__":
    inp = sys.stdin.readlines()

    grid = list(map(lambda x: x.strip(), inp))

    # Helper list to traverse adjacent cells
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    HEIGHT = len(grid)
    WIDTH = len(grid[0])

    risk_level = 0
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
                risk_level += 1 + int(grid[i][j])

    print(risk_level)
