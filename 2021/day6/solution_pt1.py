import sys

if __name__ == "__main__":
    inp = sys.stdin.readlines()

    internal_timers = list(map(int, inp[0].strip().split(",")))

    for _ in range(80):
        temp = internal_timers[:]

        for i in range(len(internal_timers)):
            temp[i] -= 1

            if temp[i] < 0:
                temp[i] = 6
                temp.append(8)

        internal_timers = temp

    print(len(internal_timers))
