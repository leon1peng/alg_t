"""
三角形最小路径和
DP
a. 重复性 （分治）： problem[i, j] = min(sub[i + 1][j], sub[i + 1][j + 1]) + a[i, j]
b. 定义状态数组 : f[i, j]
c. DP方程 : f[i, j] = min(f[i + 1, j], f[i + 1, j + 1]) + a[i, j]
"""


# 1
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]


# 2
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp =triangle
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]


# 3
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]


# 4
# 3
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]











