"""
二叉树的后序遍历
145
https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
"""


# 1
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def __init__(self):
        self.traverse_path = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.traverse_path.append(root.val)
        return self.traverse_path


# 2
class Solution:
    def __init__(self):
        self.result = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.result.append(root.val)
        return self.result


# 3
class Solution:
    def __init__(self):
        self.result = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.result.append(root.val)
        return self.result

