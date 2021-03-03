"""
N 皇后 II

"""


# 1
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, tmp, cols, pie, na):
            if row == n:
                tmp += 1
                return tmp

            for col in range(n):
                if col not in cols and row + col not in pie and row - col not in na:
                    tmp = backtrack(row + 1, tmp, cols | {col}, pie | {row + col}, na | {row - col})
            return tmp

        return backtrack(0, 0, set(), set(), set())






