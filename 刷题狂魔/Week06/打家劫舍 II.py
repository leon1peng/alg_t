"""
打家劫舍 II

DP:
    DP 方程： dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        第一个房子偷： dp1 = nums[: -1]
        第一个房子不偷: dp2 = nums[1:]
        => return max(dp1, dp2)
"""


# 1
class Solution:
    def rob(self, nums: List[int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur

        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) > 1 else nums[0]


# 2
class Solution:
    def rob(self, nums: List[int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur

        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) > 1 else nums[0]

