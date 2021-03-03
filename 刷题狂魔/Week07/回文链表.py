"""
回文链表
"""


# 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = []
        cur = head
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return res == res[::-1]


# 2
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur, res = head, []
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res == res[:: -1]
