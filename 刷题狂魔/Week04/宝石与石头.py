"""
宝石与石头
"""


# 1
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for char in S:
            if char in J:
                count += 1
        return count


# 2
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum([S.count(x) for x in J])


# 3
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum([S.count(x) for x in J])


