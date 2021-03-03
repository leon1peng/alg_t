"""
Pow(x, n)
"""


# 1
# 97.81, 70.26
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0: return 0.0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


# 2
# 递归 97.85,  84.7
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 2:
            return x*x
        if n == 0:
            return 1
        if n == -1:
            return 1/x
        if n == -2:
            return 1/(x*x)
        tmp = self.myPow(x,n//2)
        if n % 2:
            return tmp*tmp*x
        else:
            return tmp*tmp




