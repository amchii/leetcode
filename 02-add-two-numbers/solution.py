"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def add_and_carry(self, *val):
        e = sum(val)
        if e >= 10:
            e %= 10
            return e, 1
        return e, 0

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        head = result
        carry = 0
        while l1 or l2:
            if not l1:
                x = 0
                y = l2.val
            else:
                x = l1.val
                y = 0 if not l2 else l2.val
            e, next_carry = self.add_and_carry(x, y, carry)
            head.next = ListNode(e)
            head = head.next
            carry = next_carry
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            head.next = ListNode(carry)
        return result.next


class StupidSolution:
    def add_and_carry(self, *vals):
        e = sum(vals)
        carry = 0
        if e >= 10:
            e %= 10
            carry = 1
        return e, carry

    def ListNodeToList(self, l: ListNode):
        res = []
        while l is not None:
            res.append(l.val)
            l = l.next
        return res

    def ListToListNode(self, l: list):
        res = ListNode(0)
        head = res
        for i in l:
            head.next = ListNode(i)
            head = head.next
        return res.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_l1 = self.ListNodeToList(l1)
        list_l2 = self.ListNodeToList(l2)
        res = []
        len1 = len(list_l1)
        len2 = len(list_l2)
        if len1 > len2:
            max_len = len1
            list_l2.extend([0] * (len1 - len2))
        else:
            max_len = len2
            list_l1.extend([0] * (len2 - len1))
        carry = 0
        for i in range(max_len):
            e1, e2 = list_l1[i], list_l2[i]
            e, carry = self.add_and_carry(e1, e2, carry)
            res.append(e)
        if carry:
            res.append(carry)
        return self.ListToListNode(res)


def ListNodeToList(l: ListNode):
    res = []
    while l is not None:
        res.append(l.val)
        l = l.next
    return res


def ListToListNode(l: list):
    res = ListNode(0)
    head = res
    for i in l:
        head.next = ListNode(i)
        head = head.next
    return res.next


def printListNode(l):
    print(l.val, end=' ')
    if l.next:
        printListNode(l.next)


if __name__ == '__main__':
    l1 = ListToListNode([3, 5, 6])
    l2 = ListToListNode([4, 5, 7, 8])
    printListNode(Solution().addTwoNumbers(l1, l2))
