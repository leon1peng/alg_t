"""
删除排序数组中的重复项
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 1
        preNum = nums[0]
        for num in nums:
            if num != preNum:
                preNum = num
                nums[count] = num
                count += 1
        return count


# 2
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 1
        pre_num = nums[0]
        for num in nums:
            if num != pre_num:
                pre_num = num
                nums[count] = num
                count += 1
        return count


# 3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 1
        pre_num = nums[0]
        for num in nums:
            if num != pre_num:
                pre_num = num
                nums[count] = num
                count += 1
        return count


# 4
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 1
        pre_num = nums[0]
        for num in nums:
            if num != pre_num:
                pre_num = num
                nums[count] = num
                count += 1
        return count
