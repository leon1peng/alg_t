"""
环形链表 II
返回入环的第一个节点
"""


# 1
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast


# 2
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast


# 3
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while True:
            if not (fast and fast.next):
                return
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        fast = head
        while fast != slow:
            slow, fast = slow.next, fast.next
        return fast


# 4
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while True:
            if not (fast and fast.next):
                return
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        fast = head
        while fast != slow:
            slow, fast = slow.next, fast.next

        return fast


# class Solution:ss
#     def detectCycle(self, head: ListNode) -> ListNode:
#         if not head:
#             return None
#         while head.next:
#             if sys.getrefcount(head) >= 5:
#                 return head
#             head = head.next
#         return None
