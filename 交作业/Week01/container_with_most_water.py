"""
盛最多水的容器
"""

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
res, l, r = 0, 0, len(height) - 1
while l < r:
    res, l, r = (max(res,  height[l] * (r - l)), l + 1, r) if height[l] < height[r] else (max(res,  height[r] * (r - l)), l, r - 1)

print(res)

# 1
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, max_area = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                max_area = max(max_area, height[i] * (j - i))
                i += 1
            else:
                max_area = max(max_area, height[j] * (j - i))
                j -= 1
        return max_area


# 2
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, max_area = 0, len(height) - 1, 0
        while i < j:
            max_area, i, j = (max(max_area, height[i] * (j - i)), i + 1, j) if height[i] < height[j] else (max(max_area, height[j] * (j - i)), i, j - 1)
        return max_area


# 3
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, max_area = 0, len(height) - 1, 0
        while i < j:
            i, j, max_area = (i + 1, j, max(max_area, height[i] * (j - i))) if height[i] < height[j] else (i, j - 1, max(max_area, height[j] * (j - i)))
        return max_area


# 4
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, max_area = 0, len(height) - 1, 0
        while i < j:
            i, j, max_area = (i + 1, j, max(max_area, height[i] * (j - i))) if height[i] < height[j] else (i, j - 1, max(max_area, height[j] * (j - i)))
        return max_area

