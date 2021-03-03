"""
回文子串

DP
"""


# 1
# DP
class Solution:
    def __init__(self):
        self.res = 0

    def countSubstrings(self, s: str) -> int:
        n, self.res = len(s), 0

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i, j, self.res = i - 1, j + 1, self.res + 1

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return self.res


# 暴力
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                    res += 1
        return res


"""
# DP  87.10
# dp[i][j] = dp[i+1][j-1] and j-i > 1 and s[i] = s[j]
# 
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s: return 0
        res = len(s)
        dp = [[i,i+1] for i in range(len(s))]
        for i in range(1, len(s)):
            for j in dp[i-1]:
                if j-1 >= 0 and s[j-1] == s[i]:
                    res += 1
                    dp[i].append(j-1)
        return res


# 中心扩展法，分两种情况讨论 93.89      
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         L = len(s)
#         cnt = 0
#         # 以某一个元素为中心的奇数长度的回文串的情况
#         for center in range(L):
#             left = right = center
#             while left >= 0 and right < L and s[left] == s[right]:
#                 cnt += 1
#                 left -= 1
#                 right += 1
#         # 以某对元素为中心的偶数长度的回文串的情况
#         for left in range(L - 1):
#             right = left + 1
#             while left >= 0 and right < L and s[left] == s[right]:
#                 cnt += 1
#                 left -= 1
#                 right += 1

#         return cnt

"""
