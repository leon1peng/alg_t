"""
接雨水
"""


# 1
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        left, right = 0, len(height) - 1
        maxleft, maxright = height[0], height[-1]
        ans = 0

        while left <= right:
            maxleft = max(height[left], maxleft)
            maxright = max(height[right], maxright)
            if maxleft < maxright:
                ans += maxleft - height[left]
                left += 1
            else:
                ans += maxright - height[right]
                right -= 1
        return ans


# 2
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right, max_left, max_right, res = 0, len(height) - 1, height[0], height[-1], 0
        while left <= right:
            max_left, max_right = max(max_left, height[left]), max(max_right, height[right])
            if max_left < max_right:
                res += max_left - height[left]
                left += 1
            else:
                res += max_right - height[right]
                right -= 1
        return res
