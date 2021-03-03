"""
Author: Leon Peng ( 彭桂亮 )
Method: 五毒神掌
两数之和
"""


# 第一掌
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = dict()
        for index, number in enumerate(nums):
            if hashmap.get(target-number) is not None:
                return [index, hashmap.get(target-number)]
            hashmap[number] = index


# 第二掌
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for index, number in enumerate(nums):
            if hashmap.get(target-number) is not None:
                return [index, hashmap.get(target-number)]
            hashmap[number] = index


# 第三掌
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for index, number in enumerate(nums):
            if hashmap.get(target-number) is not None:
                return [index, hashmap.get(target-number)]
            hashmap[number] = index


# 4
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for index, number in enumerate(nums):
            if hashmap.get(target-number) is not None:
                return [index, hashmap.get(target-number)]
            hashmap[number] = index


# 5
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for index, number in enumerate(nums):
            if hashmap.get(target - number) is not None:
                return [index, hashmap.get(target - number)]
            hashmap[number] = index
