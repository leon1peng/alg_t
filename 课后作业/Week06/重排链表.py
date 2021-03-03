"""
重排链表
"""


# 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        pre, cur = None, slow.next
        while cur:
            temp = cur.next
            cur.next, pre, cur = pre, cur,  temp
        slow.next = None

        cur = head
        while pre:
            cur.next, pre.next, cur, pre = pre, cur.next, cur.next, pre.next
        return head


# 2
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

        pre, cur = None, slow.next
        while cur:
            temp = cur.next
            cur.next, pre, cur = pre, cur, temp
        slow.next = None
        cur = head
        while pre:
            cur.next, pre.next, cur, pre = pre, cur.next, cur.next, pre.next
        return head
