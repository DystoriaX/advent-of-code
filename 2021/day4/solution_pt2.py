from typing import List
import sys


class BingoBoard:
    BOARD_SIZE = 5

    def __init__(self, board: List[List[int]]):
        self.board = board
        self.marked = [
            [False for j in range(BingoBoard.BOARD_SIZE)]
            for i in range(BingoBoard.BOARD_SIZE)
        ]

    def mark(self, number):
        for i in range(BingoBoard.BOARD_SIZE):
            for j in range(BingoBoard.BOARD_SIZE):
                if self.board[i][j] == number:
                    self.marked[i][j] = True

    def check_horizontal(self):
        for i in range(BingoBoard.BOARD_SIZE):
            is_win = True
            for j in range(BingoBoard.BOARD_SIZE):
                is_win = is_win and self.marked[i][j]

            if is_win:
                return is_win

        return False

    def check_vertical(self):
        for j in range(BingoBoard.BOARD_SIZE):
            is_win = True
            for i in range(BingoBoard.BOARD_SIZE):
                is_win = is_win and self.marked[i][j]

            if is_win:
                return is_win

        return False

    def check_win(self):
        return self.check_horizontal() or self.check_vertical()

    def get_unmarked_sum(self):
        sum = 0
        for i in range(BingoBoard.BOARD_SIZE):
            for j in range(BingoBoard.BOARD_SIZE):
                sum += 0 if self.marked[i][j] else self.board[i][j]

        return sum

    def __str__(self) -> str:
        return repr(self.board) + "\n" + repr(self.marked)


if __name__ == "__main__":
    inp = sys.stdin.readlines()
    inp = [line.strip() for line in inp]

    number_sequence = [int(number) for number in inp[0].split(",")]
    bingo_boards: List[BingoBoard] = []

    for i in range(2, len(inp), 6):
        board = [[int(num) for num in row.split()] for row in inp[i : i + 5]]
        bingo_boards.append(BingoBoard(board))

    score = -1

    has_won = [False] * len(bingo_boards)
    for number in number_sequence:
        for [index, board] in enumerate(bingo_boards):
            board.mark(number)
            if (not has_won[index]) and board.check_win():
                has_won[index] = True
                score = board.get_unmarked_sum() * number

    print(score)
