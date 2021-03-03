"""
填充每个节点的下一个右侧节点指针
"""


# 1
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None

        def bfs(one_layer):
            next_layer = []
            for node in one_layer:
                if node.left: next_layer.append(node.left)
                if node.right: next_layer.append(node.right)
            if next_layer:
                for i in range(len(next_layer) - 1):
                    next_layer[i].next = next_layer[i + 1]
                bfs(next_layer)

        bfs([root])
        return root


# 2
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None

        def bfs(one_layer):
            next_layer = []
            for node in one_layer:
                if node.left: next_layer.append(node.left)
                if node.right: next_layer.append(node.right)
            if next_layer:
                for i in range(len(next_layer) - 1):
                    next_layer[i].next = next_layer[i + 1]
                bfs(next_layer)

        bfs([root])
        return root
