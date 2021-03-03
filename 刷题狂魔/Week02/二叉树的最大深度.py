"""
二叉树的最大深度
"""


# 1
# BFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = [(1, root)]
        while queue:
            depth, node = queue.pop(0)
            if node.left:
                queue.append((depth + 1, node.left))
            if node.right:
                queue.append((depth + 1, node.right))
        return depth


# DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        stack = [(1, root)]
        depth = 0
        while stack:
            cur_dep, node = stack.pop()
            depth = max(cur_dep, depth)
            if node.left:
                stack.append((cur_dep+1, node.left))
            if node.right:
                stack.append((cur_dep+1, node.right))
        return depth


# 2
# BFS 99.39,  99.37
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = [(1, root)]
        while queue:
            depth, node = queue.pop(0)
            if node.left:
                queue.append((depth + 1, node.left))
            if node.right:
                queue.append((depth + 1, node.right))
        return depth


# DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        depth, stack = 0, [(1, root)]
        while stack:
            cur_dp, node = stack.pop()
            depth = max(cur_dp, depth)
            if node.left:
                stack.append((cur_dp + 1, node.left))
            if node.right:
                stack.append((cur_dp + 1, node.right))
        return depth





