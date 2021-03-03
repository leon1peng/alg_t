"""
二叉搜索树的最小绝对差
"""


# 1
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        pre, cur, ans, stack = -1, root, float('inf'), []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre != -1:
                    ans = min(ans, cur.val - pre)
                pre = cur.val
                cur = cur.right
        return ans











