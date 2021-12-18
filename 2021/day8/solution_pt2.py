from typing import List, Set
import sys

"""
Convention:
    We will be using the following numbers to indicate the segments:
        0000
       1    2
       1    2
        3333
       4    5
       4    5
        6666
"""


class Query:
    def __init__(self, known: List[str], asked: List[str]):
        self.known = known
        self.asked = asked
        self.__mapping: List[Set[str]] = [set()] * 10
        self.analyze()

    def analyze(self):
        # See `analysis.md` to see the detailed analysis on how to determine mapping of each letter to the segments.

        self.__mapping[1] = set(list(next(filter(lambda x: len(x) == 2, self.known))))
        self.__mapping[4] = set(list(next(filter(lambda x: len(x) == 4, self.known))))
        self.__mapping[7] = set(list(next(filter(lambda x: len(x) == 3, self.known))))
        self.__mapping[8] = set(list(next(filter(lambda x: len(x) == 7, self.known))))

        # Determine segment two and five
        segment_two_five = self.__mapping[1] & self.__mapping[7]
        segment_two = ""
        segment_five = ""

        dig_len_6 = list(filter(lambda x: len(x) == 6, self.known))

        for dig in dig_len_6:
            dig_set = set(list(dig))
            if len(dig_set & segment_two_five) == 1:
                self.__mapping[6] = dig_set
                segment_five = next(iter(dig_set & segment_two_five))
                segment_two = next(iter(segment_two_five - dig_set))

        # Determine string digit for digit 2, 3, 5
        dig_len_5 = list(filter(lambda x: len(x) == 5, self.known))

        for dig in dig_len_5:
            has_two = segment_two in dig
            has_five = segment_five in dig

            if has_two and has_five:
                self.__mapping[3] = set(list(dig))
            elif has_two:
                self.__mapping[2] = set(list(dig))
            elif has_five:
                self.__mapping[5] = set(list(dig))
            else:
                assert False, "Logical error in determining digit 2, 3, 5"

        # Determine digit 0 and 9
        for dig in dig_len_6:
            dig_set = set(list(dig))

            if dig_set == self.__mapping[6]:
                continue
            elif len(dig_set & self.__mapping[5]) == 5:
                self.__mapping[9] = dig_set
            elif len(dig_set & self.__mapping[5]) == 4:
                self.__mapping[0] = dig_set
            else:
                assert False, "Logical error in determining digit 0, 9"

    def solve(self):
        ret = 0
        for dig_asked in self.asked:
            ret *= 10
            dig_asked_set = set(list(dig_asked))
            for number, dig_set in enumerate(self.__mapping):
                if dig_asked_set == dig_set:
                    ret += number
                    break

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
