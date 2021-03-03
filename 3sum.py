"""
三数之和
1. 数组中有无重复的元素
2. 元素顺序不一致有无关系
"""


# 1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums[:-2]):
            if num > 0: break
            if num + nums[i + 1] + nums[i + 2] > 0: break
            if num + nums[-1] + nums[-2] < 0: continue
            if i > 0 and num == nums[i - 1]: continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                tmp = num + nums[left] + nums[right]
                if tmp > 0: right -= 1
                elif tmp < 0: left += 1
                else:
                    res.append([num, nums[left], nums[right]])
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left, right = left + 1, right - 1
        return res


# 2
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, num in enumerate(nums[:-2]):
            if num > 0:
                break
            if num + nums[i + 1] + nums[i + 2] > 0:
                break
            if num + nums[-1] + nums[-2] < 0:
                continue
            if i > 0 and num == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                tmp = num + nums[left] + nums[right]
                if tmp > 0:
                    right -= 1
                elif tmp < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left, right = left + 1, right - 1
        return result


# 3
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, num in enumerate(nums[:-2]):
            if num > 0:
                break
            if num + nums[i + 1] + nums[i + 2] > 0:
                break
            if num + nums[-1] + nums[-2] < 0:
                continue
            if i > 0 and num == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                tmp = num + nums[left] + nums[right]
                if tmp > 0:
                    right -= 1
                elif tmp < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left, right = left + 1, right - 1
        return result

