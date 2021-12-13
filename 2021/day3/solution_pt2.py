import sys

if __name__ == "__main__":
    inp = sys.stdin.readlines()

    bit_length = len(inp[0]) - 1
    num_line = len(inp)

    # Finding oxygen generator rating
    candidates = inp[:]

    for i in range(bit_length):
        num_0 = 0
        num_1 = 0

        for candidate in candidates:
            if candidate[i] == "0":
                num_0 += 1
            else:
                num_1 += 1

        if num_0 <= num_1:
            candidates = list(filter(lambda candidate: candidate[i] == "1", candidates))
        else:
            candidates = list(filter(lambda candidate: candidate[i] == "0", candidates))

        if len(candidates) == 1:
            break

    oxygen_generator_rating = int(candidates[0], 2)

    # Finding CO2 scrubber rating
    candidates = inp[:]

    for i in range(bit_length):
        num_0 = 0
        num_1 = 0

        for candidate in candidates:
            if candidate[i] == "0":
                num_0 += 1
            else:
                num_1 += 1

        if num_0 <= num_1:
            candidates = list(filter(lambda candidate: candidate[i] == "0", candidates))
        else:
            candidates = list(filter(lambda candidate: candidate[i] == "1", candidates))

        if len(candidates) == 1:
            break

    co2_scrubber_rating = int(candidates[0], 2)

    print(oxygen_generator_rating * co2_scrubber_rating)
