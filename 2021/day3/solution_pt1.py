import sys

if __name__ == "__main__":
    inp = sys.stdin.readlines()

    bit_length = len(inp[0]) - 1
    num_line = len(inp)

    transpose = [[0 for j in range(num_line)] for i in range(bit_length)]

    for i in range(num_line):
        for j in range(bit_length):
            transpose[j][i] = inp[i][j]

    max_arr = list(map(lambda x: max({"0", "1"}, key=x.count), transpose))
    min_arr = list(map(lambda x: min({"0", "1"}, key=x.count), transpose))

    gamma_rate = int("".join(max_arr), 2)
    epsilon_rate = int("".join(min_arr), 2)

    print(gamma_rate * epsilon_rate)
