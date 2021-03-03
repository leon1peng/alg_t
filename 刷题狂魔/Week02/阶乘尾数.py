"""
阶乘尾数
"""


# 1
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        a = 0
        while n > 0:
            n = n // 5
            a += n
        return a


# 2
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0: return 0
        count = 0
        while n > 0:
            n = n // 5
            count += n
        return count

