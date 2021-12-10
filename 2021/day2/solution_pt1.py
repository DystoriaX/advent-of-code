import sys

if __name__ == "__main__":
    inp = sys.stdin.readlines()

    FORWARD = "forward"
    DOWN = "down"
    UP = "up"

    parsed_inp = list(map(lambda s: s.split(), inp))
    parsed_inp = list(map(lambda s: [s[0], int(s[1])], parsed_inp))

    x_pos = 0
    y_pos = 0
    for [command, step_num] in parsed_inp:
        if command == FORWARD:
            x_pos += step_num
        elif command == DOWN:
            y_pos += step_num
        elif command == UP:
            y_pos -= step_num
        else:
            sys.stderr.write(f"Unknown command: {command}")
            sys.exit(1)

    print(x_pos * y_pos)
