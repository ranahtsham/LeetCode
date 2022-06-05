# ----------------------------------------------------------------------#
# NAME: Rana Ahtsham Ul Haq                                             #
# GIT: https://github.com/ranahtsham                                    #
# LEETCODE: https://leetcode.com/ranahtsham/                            #
# LINKEDIN: https://www.linkedin.com/in/ranahtsham                      #
# ----------------------------------------------------------------------#
# DATE: Sunday, 5th June 2022                                           #
# PROBLEMS: https://leetcode.com/problems/n-queens-ii/                  #
# SUBMISSIONS: https://leetcode.com/submissions/detail/714205668/       #
# ----------------------------------------------------------------------#


class Solution:
    def totalNQueens(self, n: int) -> int:
        visited_columns = set()
        visited_diagonals = set()
        visited_anti_diagonals = set()

        def backtracking(row):
            if row == n:
                return 1

            count = 0
            for col in range(n):

                _sum = row + col
                _dif = row - col

                if not (col in visited_columns or _sum in visited_diagonals or _dif in visited_anti_diagonals):
                    visited_columns.add(col)
                    visited_diagonals.add(_sum)
                    visited_anti_diagonals.add(_dif)

                    count += backtracking(row + 1)

                    visited_columns.remove(col)
                    visited_diagonals.remove(_sum)
                    visited_anti_diagonals.remove(_dif)
            return count

        return backtracking(0)