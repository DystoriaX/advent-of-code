import sys

if __name__ == "__main__":
    inp = sys.stdin.readlines()

    positions = list(map(int, inp[0].strip().split(",")))

    positions.sort()
    median = positions[len(positions) // 2]

    ans = 0
    for position in positions:
        ans += abs(median - position)

    print(ans)
