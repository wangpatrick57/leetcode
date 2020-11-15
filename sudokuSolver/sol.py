import json
from collections import deque

NINE = 9
THREE = 3

class Solution:
    def solveSudoku(self, board: [[str]]) -> None:
        int_board = []
        blocked = []

        for r in range(NINE):
            int_board.append([])
            blocked.append([])

            for c in range(NINE):
                int_board[r].append([])
                blocked[r].append(dict())

                for i in range(1, NINE + 1):
                    int_board[r][c] = 0
                    blocked[r][c][i] = 0

        placed_vals = []

        for r in range(NINE):
            for c in range(NINE):
                val = int(board[r][c]) if board[r][c] != '.' else 0

                if val != 0:
                    placed_vals.append((r, c, val))
                    self.placeVal(int_board, r, c, val, blocked)

        if self.solveSudokuHelper(int_board, blocked):
            print('solution found!')
        else:
            print('no possible solution')

        for r in range(NINE):
            for c in range(NINE):
                board[r][c] = str(int_board[r][c]) if int_board[r][c] != 0 else '.'

        print_nice(board)
        print_blocked(blocked, False)

    def solveSudokuHelper(self, int_board: [[int]], blocked: [[{int}]]) -> bool:
        min_available = NINE + 1
        min_r = -1
        min_c = -1
        placed_vals = []

        for r in range(NINE):
            for c in range(NINE):
                if int_board[r][c] == 0:
                    num_available, available_val = self.get_num_available(blocked[r][c])

                    if num_available == 1:
                        placed_vals.append((r, c, available_val))

                        if not self.placeVal(int_board, r, c, available_val, blocked):
                            for undo_r, undo_c, undo_val in placed_vals:
                                self.unplaceVal(int_board, undo_r, undo_c, undo_val, blocked)

                            return False
                    else:
                        if num_available < min_available:
                            min_available = num_available
                            min_r = r
                            min_c = c

        if min_available == NINE + 1: # found valid solution!
            return True

        trial_vals = []

        for val, taken_num in blocked[min_r][min_c].items():
            if taken_num == 0:
                trial_vals.append(val)

        for trial_val in trial_vals:
            placed_vals.append((min_r, min_c, trial_val))

            if self.placeVal(int_board, min_r, min_c, trial_val, blocked):
                if self.solveSudokuHelper(int_board, blocked): # found solution!
                    return True

            self.unplaceVal(int_board, min_r, min_c, trial_val, blocked)
            placed_vals = placed_vals[:-1]

        int_board[min_r][min_c] = 0 # we set this at the end to save a few sets

        for undo_r, undo_c, undo_val in placed_vals:
            self.unplaceVal(int_board, undo_r, undo_c, undo_val, blocked)
            
        return False

    def placeVal(self, int_board: [[int]], r: int, c: int, val: int, blocked: [[{int}]]) -> bool:
        assert int_board[r][c] == 0 # PAT DEBUG
        int_board[r][c] = val # place val when you know it's good
        valid = True

        for rorc in range(NINE):
            if rorc != r:
                if not self.removeWithCheck(blocked, rorc, c, val):
                    valid = False

            if rorc != c:
                if not self.removeWithCheck(blocked, r, rorc, val):
                    valid = False

        start_r = (r // 3) * 3
        start_c = (c // 3) * 3

        for dr in range(THREE):
            for dc in range(THREE):
                curr_r = start_r + dr
                curr_c = start_c + dc

                if not (curr_r == r and curr_c == c):
                    if not self.removeWithCheck(blocked, curr_r, curr_c, val):
                        valid = False

        return valid

    def unplaceVal(self, int_board: [[int]], r: int, c: int, val: int, blocked: [[{int}]]) -> None:
        assert int_board[r][c] == val # PAT DEBUG
        int_board[r][c] = 0 # place val when you know it's good

        for rorc in range(NINE):
            if rorc != r:
                blocked[rorc][c][val] -= 1

            if rorc != c:
                blocked[r][rorc][val] -= 1

        start_r = (r // 3) * 3
        start_c = (c // 3) * 3

        for dr in range(THREE):
            for dc in range(THREE):
                curr_r = start_r + dr
                curr_c = start_c + dc

                if not (curr_r == r and curr_c == c):
                    blocked[curr_r][curr_c][val] -= 1

    def removeWithCheck(self, blocked: [[{int}]], r: int, c: int, val: int) -> bool:
        blocked[r][c][val] += 1

        if self.get_num_available(blocked[r][c])[0] == 0:
            return False

        return True

    def get_num_available(self, cell_blocked: {int: int}) -> (int, int):
        num_available = 0
        available_val = 0

        for k, v in cell_blocked.items():
            if v == 0:
                num_available += 1
                available_val = k

        return (num_available, available_val)

def print_nice(board: [[int]]) -> None:
    for r in range(NINE):
        for c in range(NINE):
            print(board[r][c], ' ', end = '')

        print()

def print_blocked(blocked: [[{int}]], show_blocked: bool) -> None:
    for r in range(NINE):
        for c in range(NINE):
            if show_blocked:
                print({i for i in range(1, NINE + 1) if blocked[r][c][i] != 0}, ' ', end = '')
            else:
                print({i for i in range(1, NINE + 1) if blocked[r][c][i] == 0}, ' ', end = '')

        print()

board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
sol = Solution()
sol.solveSudoku(board)
