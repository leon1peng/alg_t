"""
反转链表
"""


# 1
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next, pre, cur = pre, cur,  temp
        return pre


# 2
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            temp = cur.next
            cur.next, pre, cur = pre, cur, temp
        return pre


# 3
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            temp = cur.next
            cur.next, pre, cur = pre, cur, temp
        return pre
