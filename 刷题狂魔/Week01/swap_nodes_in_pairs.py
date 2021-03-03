"""
Author: Leon Peng ( 彭桂亮 )
Method: 五毒神掌
两两交换链表中的节点
"""


# 第一掌
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        cur = pre
        while cur.next and cur.next.next:
            first = cur.next
            second = first.next
            cur.next, first.next, second.next = second, second.next, first
            cur = cur.next.next
        return pre.next
    


# 第二掌
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        cur = pre
        while cur.next and cur.next.next:
            first = cur.next
            second = first.next
            cur.next, first.next, second.next = second, second.next, first
            cur = cur.next.next
        return pre.nexts


# 第三掌
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        cur = pre
        while cur.next and cur.next.next:
            first = cur.next
            second = first.next
            first.next, second.next, cur.next = second.next, first, second
            cur = cur.next.next
        return pre.next


# 4
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        cur = pre
        while cur.next and cur.next.next:
            first = cur.next
            second = first.next
            first.next, second.next, cur.next = second.next, first, second
            cur = cur.next.next
        return pre.next


# 5
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        cur = pre
        while cur.next and cur.next.next:
            first = cur.next
            second = first.next
            first.next, second.next, cur.next = second.next, first, second
            cur = cur.next.next
        return pre.next


# 6
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        cur = pre
        while cur.next and cur.next.next:
            first = cur.next
            second = first.next
            first.next, second.next, cur.next = second.next, first, second
            cur = cur.next.next
        return pre.next


# 7
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        cur = pre
        while cur.next and cur.next.next:
            first = cur.next
            second = first.next
            first.next, second.next, cur.next = second.next, first, second
            cur = cur.next.next
        return pre.next

