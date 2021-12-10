import sys

if __name__ == "__main__":
    inp = sys.stdin.readlines()

    measured_depth = list(map(int, inp))
    measured_depth = [
        measured_depth[i] + measured_depth[i + 1] + measured_depth[i + 2]
        for i in range(len(measured_depth) - 2)
    ]

    ans = 0
    prev_num = measured_depth[0]

    for num in measured_depth[1:]:
        if prev_num < num:
            ans += 1

        prev_num = num

    print(ans)
