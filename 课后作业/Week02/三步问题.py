"""
三步问题

DP:
    DP 方程: dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
"""


# 1
class Solution:
    def waysToStep(self, n: int) -> int:
        if n <= 2: return n
        a, b, c = 1, 1, 2
        for i in range(3, n+1):
            a, b, c = b, c, (a+b+c) % 1000000007
        return c


# 2
class Solution:
    def waysToStep(self, n: int) -> int:
        if n <= 2: return n
        a, b, c = 1, 1, 2
        for i in range(3, n+1):
            a, b, c = b, c, (a+b+c) % 1000000007
        return c




