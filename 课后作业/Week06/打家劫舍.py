"""
打家劫舍

DP
解法 I:
    a[i][0, 1] : 0 -> 不偷， 1 -> 偷
    a[0][0] = 0
    a[0][1] = 1

    a[i][0] = max(a[i - 1][0], a[i - 1][1])
    a[i][1] = a[i - 1][0] + nums[i]

解法 II:
    a[i] : 可偷可不偷

    a[i] = max(a[i - 1], nums[i] + a[i - 2])
"""


# 1
# 解法 II:
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = now = 0
        for i in nums:
            # dp = max(dp[i - 1], nums[i] + dp[i - 2])
            pre, now = now, max(pre + i, now)
        return now


# 解法 I:
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        a = [[0, 0] for i in range(len(nums))]
        a[0][1] = nums[0]
        for i in range(1, n):
            a[i][0] = max(a[i - 1][0], a[i - 1][1])
            a[i][1] = a[i - 1][0] + nums[i]
        return max(a[n - 1][0], a[n - 1][1])


# 2
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = now = 0
        for i in nums:
            pre, now = now, max(pre + i, now)
        return now


# 3
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre, now = 0, 0
        for i in nums:
            pre, now = now, max(now, pre + i)
        return now


# 4
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre, now = 0, 0
        for i in nums:
            pre, now = now, max(now, pre + i)
        return now





