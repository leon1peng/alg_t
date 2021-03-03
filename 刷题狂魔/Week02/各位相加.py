"""
各位相加
"""


# 1
class Solution:
    def addDigits(self, num: int) -> int:
        res = 0
        for char in str(num):
            res += int(char)
        if res > 9:
            res = self.addDigits(res)
        return res


# 2
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            return (num - 1) % 9 + 1


# 3
class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else (num - 1) % 9 + 1


# 4
class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else (num - 1) % 9 + 1


# 5
class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else (num - 1) % 9 + 1


