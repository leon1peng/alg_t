"""
删除链表的倒数第N个节点
"""


# 1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 快慢指针
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = ListNode(0)
        pre.next = head

        slow, fast = pre, pre
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return pre.next


# 递归迭代 -- 回溯时，进行节点计数
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            self.count = 0
            return head
        head.next = self.removeNthFromEnd(head.next, n)
        self.count += 1
        return head.next if self.count == n else head


