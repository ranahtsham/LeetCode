# ----------------------------------------------------------------------#
# NAME: Rana Ahtsham Ul Haq                                             #
# GIT: https://github.com/ranahtsham                                    #
# LEETCODE: https://leetcode.com/ranahtsham/                            #
# LINKEDIN: https://www.linkedin.com/in/ranahtsham                      #
# ----------------------------------------------------------------------#
# DATE: Friday, 3 June 2022                                             #
# PROBLEMS: https://leetcode.com/problems/range-sum-query-2d-immutable/ #
# SUBMISSIONS: https://leetcode.com/submissions/detail/713523060/       #
# ----------------------------------------------------------------------#


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.matrix = matrix
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        if rows == 0 or cols == 0:
            return

        self.cashing = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(rows):
            for j in range(cols):
                self.cashing[i + 1][j + 1] = self.cashing[i + 1][j] + self.cashing[i][j + 1] + \
                                             self.matrix[i][j] -  self.cashing[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return int(self.cashing[row2 + 1][col2 + 1] - self.cashing[row1][col2 + 1] - \
                   self.cashing[row2 + 1][col1] + self.cashing[row1][col1])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)