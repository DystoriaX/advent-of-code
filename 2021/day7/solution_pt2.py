import sys


def get_cost(arr, x):
    cost = 0
    for number in arr:
        diff = abs(number - x)
        cost += diff * (diff + 1) // 2

    return cost


if __name__ == "__main__":
    inp = sys.stdin.readlines()

    positions = list(map(int, inp[0].strip().split(",")))

    max_pos = max(positions)
    min_pos = min(positions)

    ans = float("inf")
    for position in range(min_pos, max_pos + 1):
        ans = min(ans, get_cost(positions, position))

    print(ans)
