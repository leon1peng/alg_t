"""
有序数组的平方
"""


# 1
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans, left, right, cur = [0] * len(A), 0, len(A) - 1, len(A) - 1
        while left <= right:
            if abs(A[left]) > abs(A[right]):
                ans[cur], left = A[left] ** 2, left + 1
            else:
                ans[cur], right = A[right] ** 2, right - 1
            cur -= 1
        return ans


# 2
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(num * num for num in A)


# 3
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(num * num for num in A)


