"""
滑动窗口最大值
"""


# 1
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque, result = [], []
        for i in range(0, len(nums)):
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
            deque.append(i)
            while i - deque[0] > k - 1:
                deque.pop(0)
            if i >= k - 1:
                result.append(nums[deque[0]])
        return result


# 2
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue, result = nums[: k], []
        for i in range(len(nums)):
            result.append(max(queue))
            if i + k >= len(nums):
                return result
            queue.pop(0)
            queue.append(nums[i + k])
        return result


# 3
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque, result = [], []
        for i in range(len(nums)):
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
            deque.append(i)
            while i-deque[0] > k-1:
                deque.pop(0)
            if i >= k - 1:
                result.append(nums[deque[0]])
        return result


# 4
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque, result = [], []
        for i in range(0, len(nums)):
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()

            deque.append(i)

            while i - deque[0] > k - 1:
                deque.pop(0)

            if i >= k - 1:
                result.append(nums[deque[0]])
        return result


# 5
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque, result = [], []
        for i in range(0, len(nums)):
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()

            deque.append(i)

            while i - deque[0] > k - 1:
                deque.pop(0)

            if i >= k - 1:
                result.append(nums[deque[0]])
        return result








