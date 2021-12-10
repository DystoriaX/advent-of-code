import sys

if __name__ == "__main__":
    inp = sys.stdin.readlines()

    measured_depth = list(map(int, inp))

    ans = 0
    prev_num = measured_depth[0]

    for num in measured_depth[1:]:
        if prev_num < num:
            ans += 1

        prev_num = num

    print(ans)
