"""
柠檬水找零
"""


# 1
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        i = j = 0
        for k in bills:
            if k == 5:
                i += 1
            elif k == 10:
                i, j = i - 1, j + 1
            else:
                if j == 0:
                    i -= 3
                else:
                    i, j = i - 1, j - 1
            if i < 0 or j < 0:
                return False
        return True


# 2
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        i, j = 0, 0
        for bill in bills:
            if bill == 5:
                i += 1
            elif bill == 10:
                i, j = i - 1, j + 1
            else:
                if j == 0:
                    i -= 3
                else:
                    i, j = i - 1, j - 1
            if i < 0:
                return False
        return True