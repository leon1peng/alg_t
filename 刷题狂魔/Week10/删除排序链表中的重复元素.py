"""
删除排序链表中的重复元素
"""


# 1
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 递归
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if head.next and head.val == head.next.val:
            while head.next is not None and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head)
        else:
            head.next = self.deleteDuplicates(head.next)
        return head


# 双指针
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = ListNode(-1000)
        pre.next = head
        slow = pre
        fast = pre.next
        while fast:
            if slow.val == fast.val:
                fast = fast.next
                slow.next = fast
            else:
                slow = slow.next
                fast = fast.next
        return pre.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = head
        while pre and pre.next:
            if pre.val == pre.next.val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return head


# 2
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = head
        while pre and pre.next:
            if pre.val == pre.next.val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return head


# 3
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = head
        while pre and pre.next:
            if pre.val == pre.next.val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return head


# 4
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = head
        while pre and pre.next:
            if pre.val == pre.next.val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return head


