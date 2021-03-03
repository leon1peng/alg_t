"""
二叉树的前序遍历
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.traverse_path = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.traverse_path.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.traverse_path

