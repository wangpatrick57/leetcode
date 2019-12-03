class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        # rows
        for r in range(9):
            this_row_nums = set()

            for c in range(9):
                this_str = board[r][c]

                if this_str != '.':
                    if this_str in this_row_nums:
                        return False

                    this_row_nums.add(this_str)

        # cols
        for c in range(9):
            this_row_nums = set()

            for r in range(9):
                this_str = board[r][c]

                if this_str != '.':
                    if this_str in this_row_nums:
                        return False

                    this_row_nums.add(this_str)

        # squares
        for r_origin in range(3):
            for c_origin in range(3):
                this_row_nums = set()

                for dr in range(3):
                    for dc in range(3):
                        r = r_origin * 3 + dr
                        c = c_origin * 3 + dc

                        this_str = board[r][c]

                        if this_str != '.':
                            if this_str in this_row_nums:
                                return False

                            this_row_nums.add(this_str)

        return True
