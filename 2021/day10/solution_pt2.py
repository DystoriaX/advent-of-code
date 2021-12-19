from collections import deque
from typing import List
import sys

if __name__ == "__main__":
    inp = sys.stdin.readlines()

    syntaxes = list(map(lambda x: x.strip(), inp))

    stack = deque()
    OPENING_BRACKETS = ["(", "[", "{", "<"]
    CLOSING_BRACKETS = [")", "]", "}", ">"]
    SCORE_MAPPING = {"(": 1, "[": 2, "{": 3, "<": 4}

    scores: List[int] = []

    for syntax in syntaxes:
        stack.clear()
        is_incomplete = True
        for bracket in syntax:
            if bracket in OPENING_BRACKETS:
                stack.append(bracket)
            elif bracket in CLOSING_BRACKETS:
                last_opening_bracket = stack.pop()
                if (
                    last_opening_bracket
                    != OPENING_BRACKETS[CLOSING_BRACKETS.index(bracket)]
                ):
                    is_incomplete = False
                    break
            else:
                assert False, f"Illegal bracket found: {bracket}"

        if not is_incomplete:
            continue

        current_score = 0
        while len(stack) > 0:
            current_score = current_score * 5 + SCORE_MAPPING[stack.pop()]

        scores.append(current_score)

    scores.sort()
    print(scores[len(scores) // 2])
