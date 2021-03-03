"""
零钱兑换

1. 暴力： 递归
2. BFS
3. DP
    a. 重复性（子问题）： problem[i] = min(sub[i - k] for k in [1, 2, 5])
    b. DP 数组： f[i]
    c. DP 方程： f[i] = min(f[i - k] for k in [1, 2, 5]) + 1
"""


# 1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float("inf")
        dp = [0] + [MAX] * amount
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - k] if i - k >= 0 else MAX for k in coins]) + 1
        return [dp[amount], - 1][dp[amount] == MAX]


# 2
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_num = float("inf")
        dp = [0] + [max_num] * amount
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - k] if i - k >= 0 else max_num for k in coins]) + 1
        return [dp[amount], - 1][dp[amount] == max_num]


# 3
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_num = float("inf")
        dp = [0] + [max_num] * amount
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - k] if i - k >= 0 else max_num for k in coins]) + 1
        return [dp[amount], - 1][dp[amount] == max_num]









