"""
长按键入
"""


# 1
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, name = 0, name + "1"
        for s in typed:
            if s == name[i]:
                i += 1
            elif s != name[i - 1]:
                return False
        return i == len(name) - 1

