import sys

NUM_DAYS = 256
MAX_SIZE = 300
MAX_DAY = 8

dp = [[-1 for _ in range(MAX_DAY + 1)] for _ in range(MAX_SIZE + 1)]
num = [0] * (MAX_DAY + 1)


# Calculates the number of fish at day `day` which will bear a new one
# in `time_left` day(s).
def total_fish(day, time_left):
    if day < 0 or time_left > MAX_DAY:
        return 0
    elif day == 0:
        return num[time_left]
    elif dp[day][time_left] != -1:
        return dp[day][time_left]

    dp[day][time_left] = total_fish(day - 1, time_left + 1)

    # New born
    if time_left == 8:
        dp[day][time_left] += total_fish(day - 1, 0)

    # The one who bears
    if time_left == 6:
        dp[day][time_left] += total_fish(day - 1, 0)

    return dp[day][time_left]


if __name__ == "__main__":
    inp = sys.stdin.readlines()

    internal_timers = list(map(int, inp[0].strip().split(",")))

    total = 0

    for timer in internal_timers:
        num[timer] += 1

    for i in range(MAX_DAY + 1):
        total += total_fish(NUM_DAYS, i)

    print(total)
