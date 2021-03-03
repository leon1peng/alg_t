"""
N叉树的层序遍历
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            result.append(node.val for node in queue)
            queue = [child for node in queue for child in node.children]
        return result


# 2
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        queue, result = [root], []
        while queue:
            result.append(node.val for node in queue)
            queue = [child for node in queue for child in node.children]
        return result
