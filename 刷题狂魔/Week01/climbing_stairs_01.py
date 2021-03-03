"""
Author: Leon Peng ( 彭桂亮 )
Method: 五毒神掌
"""


# 第一掌
class Solution:
    hashmap = dict()

    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 2:
            return n
        if self.hashmap.get(n) is not None:
            return self.hashmap[n]
        self.hashmap[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# 第二掌
class Solution:
    hashmap = dict()

    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 2:
            return n
        if self.hashmap.get(n) is not None:
            return self.hashmap[n]
        self.hashmap[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# 3
class Solution:
    hashmap = dict()

    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 2:
            return n
        if self.hashmap.get(n) is not None:
            return self.hashmap[n]
        self.hashmap[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# 4
class Solution:
    hashmap = dict()

    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 2:
            return n

        if self.hashmap.get(n) is not None:
            return self.hashmap[n]
        self.hashmap[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.hashmap[n]


# 5
class Solution:
    hashmap = dict()

    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 2:
            return n
        if self.hashmap.get(n) is not None:
            return self.hashmap[n]
        self.hashmap[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.hashmap[n]



