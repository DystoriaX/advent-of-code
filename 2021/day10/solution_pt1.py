from collections import deque
import sys

if __name__ == "__main__":
    inp = sys.stdin.readlines()

    syntaxes = list(map(lambda x: x.strip(), inp))

    stack = deque()
    OPENING_BRACKETS = ["(", "[", "{", "<"]
    CLOSING_BRACKETS = [")", "]", "}", ">"]
    SCORE_MAPPING = {")": 3, "]": 57, "}": 1197, ">": 25137}

    score = 0

    for syntax in syntaxes:
        stack.clear()
        for bracket in syntax:
            if bracket in OPENING_BRACKETS:
                stack.append(bracket)
            elif bracket in CLOSING_BRACKETS:
                last_opening_bracket = stack.pop()
                if (
                    last_opening_bracket
                    != OPENING_BRACKETS[CLOSING_BRACKETS.index(bracket)]
                ):
                    score += SCORE_MAPPING[bracket]
                    break
            else:
                assert False, f"Illegal bracket found: {bracket}"

    print(score)
