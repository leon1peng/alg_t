"""
按奇偶排序数组 II
"""
from typing import List


# 1
# 95.6  5.35
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd_list, even_list, result = [], [], []
        for num in A:
            if num % 2 == 0:
                even_list.append(num)
            else:
                odd_list.append(num)
        for i in range(len(odd_list)):
            result.append(even_list[i])
            result.append(odd_list[i])
        return result


# 91.19    45.26
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        nums1 = list(filter(lambda a: a % 2 == 0, A))
        nums2 = list(filter(lambda a: a % 2 == 1, A))
        A[::2], A[1::2] = nums1, nums2
        return A


# 2
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd_list, even_list, res = [], [], []
        for i in A:
            if i % 2 == 0:
                even_list.append(i)
            else:
                odd_list.append(i)
        for i in range(len(odd_list)):
            res.append(even_list[i])
            res.append(odd_list[i])
        return res


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        nums1 = list(filter(lambda x: x % 2 == 0, A))
        nums2 = list(filter(lambda x: x % 2 == 1, A))
        A[:: 2], A[1:: 2] = nums1, nums2
        return A


# 3
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd, even, res = [], [], []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(len(odd)):
            res.append(even[i])
            res.append(odd[i])
        return res


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        nums1 = list(filter(lambda x: x % 2 == 0, A))
        nums2 = list(filter(lambda x: x % 2 == 1, A))
        A[::2], A[1::2] = nums1, nums2
        return A

