"""
K 个一组 翻转链表
"""


class Solution:
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        cur = head
        while prev != tail:
            temp = cur.next
            cur.next, prev, cur = prev, cur, temp
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)

            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next


# 2
class Solution:
    def reverse(self, head: ListNode, tail: ListNode):
        prev, cur = tail.next, head
        while prev != tail:
            temp = cur.next
            cur.next, prev, cur = prev, cur, temp
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair, hair.next = ListNode(0), head
        pre = hair

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)

            pre.next, tail.next, pre, head = head, nex, tail, tail.next

        return hair.next


# 3
class Solution:
    def reverse(self, head: ListNode, tail: ListNode):
        prev, cur = tail.next, head
        while prev != tail:
            temp = cur.next
            cur.next, prev, cur = prev, cur, temp
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair, hair.next = ListNode(0), head
        pre = hair

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)

            pre.next, tail.next, pre, head = head, nex, tail, tail.next

        return hair.next


# 4
class Solution:
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        cur = head
        while prev != tail:
            temp = cur.next
            cur.next, prev, cur = prev, cur, temp
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair, hair.next = ListNode(0), head
        pre = hair
        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            pre.next, pre, head = head, tail, nex
        return hair.next

