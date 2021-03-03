"""
买卖股票的最佳时机 II
"""


# 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            temp = prices[i] - prices[i - 1]
            if temp > 0:
                profit += temp
        return profit


# 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            temp = prices[i] - prices[i - 1]
            if temp > 0:
                profit += temp
        return profit
