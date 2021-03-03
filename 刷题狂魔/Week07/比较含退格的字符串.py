"""
比较含退格的字符串
"""


# 1
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        res = ["", ""]
        for i, char in enumerate([S, T]):
            for c in char:
                if c == "#":
                    if res[i]:
                        res[i] = res[i][: -1]
                else:
                    res[i] = res[i] + c
        return res[0] == res[1]


# 2
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        res = ["", ""]
        for i, char in enumerate([S, T]):
            for c in char:
                if c == "#":
                    if res[i]:
                        res[i] = res[i][: -1]
                else:
                    res[i] = res[i] + c
        return res[0] == res[1]
