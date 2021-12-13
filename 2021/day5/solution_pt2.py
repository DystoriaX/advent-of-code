from typing import List
import sys


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class LineSegment:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

        # Guarantees that the starting point is to the left the terminating point
        if self.start.x > self.end.x or self.start.y > self.end.y:
            self.start, self.end = self.end, self.start

    def is_straight(self):
        return self.start.x == self.end.x or self.start.y == self.end.y

    def __repr__(self):
        return f"Line Segment: [{self.start}, {self.end}]"


if __name__ == "__main__":
    inp = sys.stdin.readlines()

    line_segments: List[LineSegment] = []

    for line in inp:
        [start, end] = line.strip().split(" -> ")
        start = list(map(int, start.split(",")))
        end = list(map(int, end.split(",")))

        line_segment = LineSegment(Point(*start), Point(*end))
        line_segments.append(line_segment)

    max_x = 0
    max_y = 0
    for line_segment in line_segments:
        max_x = max(max_x, line_segment.start.x, line_segment.end.x)
        max_y = max(max_y, line_segment.start.y, line_segment.end.y)

    # 0-indexing, hence the size must add 1
    field = [[0] * (max_x + 1) for _ in range(max_y + 1)]

    for line_segment in line_segments:
        start = line_segment.start
        end = line_segment.end

        if start.x == end.x:
            for y in range(start.y, end.y + 1):
                field[y][start.x] += 1
        elif start.y == end.y:
            for x in range(start.x, end.x + 1):
                field[start.y][x] += 1
        else:
            sgn_x = -1 if end.x - start.x < 0 else 1
            sgn_y = -1 if end.y - start.y < 0 else 1

            pt_x = start.x
            pt_y = start.y

            while pt_x != end.x or pt_y != end.y:
                field[pt_y][pt_x] += 1

                pt_x += sgn_x
                pt_y += sgn_y

            field[pt_y][pt_x] += 1

    count = 0

    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] > 1:
                count += 1

    print(count)
