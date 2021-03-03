"""
N 皇后

回溯
"""


# 1
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, cur_str = [], "." * n

        def backtrack(row, tmp, cols, pie, na):
            if row == n:
                res.append(tmp)
                return

            for col in range(n):
                if col not in cols and row + col not in pie and row - col not in na:
                    backtrack(row + 1, tmp + [cur_str[:col] + "Q" + cur_str[col + 1:]], cols | {col}, pie | {row + col}, na | {row - col})

        backtrack(0, [], set(), set(), set())
        return res















