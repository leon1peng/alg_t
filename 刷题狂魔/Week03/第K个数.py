"""
第K个数
17.09
https://leetcode-cn.com/problems/get-kth-magic-number-lcci/
动态规划，还没复习到，先“抄”答案
"""


# 1
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        res = [1] * k
        idx3, idx5, idx7 = 0, 0, 0
        for i in range(1, k):
            res[i] = min(res[idx3]*3, res[idx5]*5, res[idx7]*7)
            if res[i] == res[idx3]*3: idx3 += 1
            if res[i] == res[idx5]*5: idx5 += 1
            if res[i] == res[idx7]*7: idx7 += 1
        return res[k-1]




