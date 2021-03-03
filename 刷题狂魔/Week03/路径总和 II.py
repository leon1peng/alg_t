"""
路径总和 II
"""


# 1
class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        if not root: return []
        stack = [([root.val], root)]
        res = []
        while stack:
            tmp, node = stack.pop()
            if not node.right and not node.left and sum(tmp) == sum_:
                res.append(tmp)
            if node.right:
                stack.append((tmp + [node.right.val], node.right))
            if node.left:
                stack.append((tmp + [node.left.val], node.left))
        return res


# 2
class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        if not root:
            return []
        stack = [([root.val], root)]
        result = []
        while stack:
            temp, node = stack.pop()
            if not node.left and not node.right and sum(temp) == sum_:
                result.append(temp)
            if node.right:
                stack.append((temp + [node.right.val], node.right))
            if node.left:
                stack.append((temp + [node.left.val], node.left))
        return result


# 3
class Solution:
    def pathSum(self, root: TreeNode, sums: int) -> List[List[int]]:
        if not root:
            return []
        result, stack = [], [([root.val], root)]
        while stack:
            temp, node = stack.pop()
            if not node.left and not node.right and sum(temp) == sums:
                result.append(temp)
            if node.left:
                stack.append((temp + [node.left.val], node.left))
            if node.right:
                stack.append((temp + [node.right.val], node.right))
        return result


