# coding=utf8
# 题目: 判断一个链表是否有环
# 思路:

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = head
        faster = head.next
        while faster and faster.next and slow != faster:
            slow = slow.next
            faster = faster.next.next
        return slow == faster and faster != None and faster.next != None


