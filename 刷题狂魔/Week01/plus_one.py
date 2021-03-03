"""
Author: Leon Peng ( 彭桂亮 )
Method: 五毒神掌
"""


# 第一掌
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        sum_num = 0
        for i in range(len(digits)):
            sum_num += digits[i] * pow(10, len(digits)-i-1)
        return [int(num) for num in str(sum_num+1)]


# 第二掌
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        sum_num = 0
        for i in range(len(digits)):
            sum_num += digits[i] * pow(10, len(digits)-i-1)
        return [int(num) for num in str(sum_num+1)]


# 3
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum_num = 0
        for i in range(len(digits)):
            sum_num += digits[i] * pow(10, len(digits)-1-i)
        return [int(num) for num in str(sum_num+1)]


# 4
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum_num = 0
        for i in range(len(digits)):
            sum_num += digits[i] * pow(10, len(digits) - 1 - i)
        return [int(num) for num in str(sum_num+1)]


# 5
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum_num = 0
        for i in range(len(digits)):
            sum_num += digits[i] * pow(10, len(digits) - 1 - i)
        return [int(num) for num in str(sum_num + 1)]
