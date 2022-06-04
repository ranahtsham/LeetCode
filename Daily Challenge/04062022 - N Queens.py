# ----------------------------------------------------------------------#
# NAME: Rana Ahtsham Ul Haq                                             #
# GIT: https://github.com/ranahtsham                                    #
# LEETCODE: https://leetcode.com/ranahtsham/                            #
# LINKEDIN: https://www.linkedin.com/in/ranahtsham                      #
# ----------------------------------------------------------------------#
# DATE: Saturday, 4th June 2022                                         #
# PROBLEMS: https://leetcode.com/problems/n-queens/                     #
# SUBMISSIONS: https://leetcode.com/submissions/detail/714205668/       #
# ----------------------------------------------------------------------#


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chessboard = [['.'] * n for _ in range(n)]
        success_results = []

        visited_columns = set()
        visited_diagonals = set()
        visited_antidiagonals = set()

        def backtrack(row):
            if row == n:
                success_results.append([''.join(state) for state in chessboard])
                return

            for col in range(n):
                _sum = row - col
                _dif = row + col

                if not (col in visited_columns or
                        _sum in visited_diagonals or
                        _dif in visited_antidiagonals):
                    visited_columns.add(col)
                    visited_diagonals.add(_sum)
                    visited_antidiagonals.add(_dif)
                    chessboard[row][col] = 'Q'

                    backtrack(row + 1)

                    visited_columns.remove(col)
                    visited_diagonals.remove(_sum)
                    visited_antidiagonals.remove(_dif)
                    chessboard[row][col] = '.'

        backtrack(0)
        return success_results
