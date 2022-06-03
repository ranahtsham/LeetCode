# ----------------------------------------------------------------------#
# NAME: Rana Ahtsham Ul Haq                                             #
# GIT: https://github.com/ranahtsham                                    #
# LEETCODE: https://leetcode.com/ranahtsham/                            #
# LINKEDIN: https://www.linkedin.com/in/ranahtsham                      #
# ----------------------------------------------------------------------#
# DATE: Thursday, 2 June 2022                                           #
# PROBLEMS: https://leetcode.com/problems/transpose-matrix/             #
# SUBMISSIONS: https://leetcode.com/submissions/detail/712929364/       #
# ----------------------------------------------------------------------#

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        m = len(matrix)
        n = len(matrix[0])

        new_matrix = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                new_matrix[j][i] = matrix[i][j]
        del matrix
        return new_matrix