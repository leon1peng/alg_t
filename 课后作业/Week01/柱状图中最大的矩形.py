"""
柱状图中最大的矩形
"""


# 1
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        result = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                result = max(result, (i - stack[-1] - 1) * heights[index])
            stack.append(i)
        return result


# 2
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, heights, result = [], [0] + heights + [0], 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                result = max(result, (i - stack[-1] - 1) * heights[index])
            stack.append(i)
        return result


# 3
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, heights, result = [], [0] + heights + [0], 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                result = max(result, (i - stack[-1] - 1) * heights[index])
            stack.append(i)
        return result
