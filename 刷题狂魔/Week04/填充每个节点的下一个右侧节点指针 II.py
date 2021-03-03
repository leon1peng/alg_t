"""
填充每个节点的下一个右侧节点指针 II
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


# 1
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        while head:
            cur = head
            pre = head = None
            while cur:
                if cur.left:
                    if not pre:
                        pre = head =cur.left
                    else:
                        pre.next = cur.left
                        pre = pre.next
                if cur.right:
                    if not pre:
                        pre = head = cur.right
                    else:
                        pre.next = cur.right
                        pre = pre.next
                cur = cur.next
        return root


# 2
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        def BFS(oneLayer):
            nextLayer = []
            for node in oneLayer:
                if node.left:
                    nextLayer.append(node.left)
                if node.right:
                    nextLayer.append(node.right)
            if len(nextLayer) > 1:
                for i in range(len(nextLayer) - 1):
                    nextLayer[i].next = nextLayer[i + 1]
            if nextLayer:
                BFS(nextLayer)
        BFS([root])
        return root


# 3
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        def bfs(one_layer):
            next_layer = []
            for node in one_layer:
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            if next_layer:
                for i in range(len(next_layer) - 1):
                    next_layer[i].next = next_layer[i + 1]
                bfs(next_layer)
        bfs([root])
        return root


# 4
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        def bfs(one_layer):
            next_layer = []
            for node in one_layer:
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            if next_layer:
                for i in range(len(next_layer) - 1):
                    next_layer[i].next = next_layer[i + 1]
                bfs(next_layer)
        bfs([root])
        return root


