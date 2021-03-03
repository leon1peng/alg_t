"""
最长上升子序列
"""


# 1
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if dp[m] < num:
                    i = m + 1
                else:
                    j = m
            dp[i] = num
            if j == res:
                res += 1
        return res



