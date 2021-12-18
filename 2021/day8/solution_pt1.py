from typing import List
import sys


class Query:
    def __init__(self, known: List[str], asked: List[str]):
        self.known = known
        self.asked = asked

    def is_one(self, digit: str):
        return len(digit) == 2

    def is_four(self, digit: str):
        return len(digit) == 4

    def is_seven(self, digit: str):
        return len(digit) == 3

    def is_eight(self, digit: str):
        return len(digit) == 7

    def solve(self):
        ret = 0

        for digit_str in self.asked:
            if (
                self.is_one(digit_str)
                or self.is_four(digit_str)
                or self.is_seven(digit_str)
                or self.is_eight(digit_str)
            ):
                ret += 1

        return ret

    def __repr__(self):
        return f"Known: {self.known}\nAsked: {self.asked}"


if __name__ == "__main__":
    inp = sys.stdin.readlines()

    queries = []
    for line in inp:
        known_str, asked_str = line.split("|")
        queries.append(Query(known_str.strip().split(), asked_str.strip().split()))

    ans = 0
    for query in queries:
        ans += query.solve()

    print(ans)
