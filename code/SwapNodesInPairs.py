# coding=utf8
# 题目: 给定链表,将链表的相邻的两个节点进行交换,不能交换值,只能改变指针
# 思路:

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        last = None
        current = head
        while current and current.next:
            nextnext = current.next.next
            current.next.next = current
            if last == None:
                new_head = current.next
            else:
                last.next = current.next
            last = current
            current = nextnext
        last.next = current

        return new_head
