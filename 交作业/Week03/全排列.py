"""
全排列
46
https://leetcode-cn.com/problems/permutations/
"""


# 1
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            # recursion terminator
            if depth == size:
                res.append(path[:])
                return
            # prepare data
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, path, used, res)

                    used[i] = False
                    path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        dfs(nums, size, 0, [], used, res)
        return res


# 2
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def DFS(nums, size, depth, cur_res, used, res):
            if depth == size:
                res.append(cur_res[:])
                return
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    cur_res.append(nums[i])
                    DFS(nums, size, depth + 1, cur_res, used, res)
                    used[i] = False
                    cur_res.pop()
        size = len(nums)
        if size == 0:
            return []
        used, res = [False for _ in range(size)], []
        DFS(nums, size, 0, [], used, res)
        return res
