# coding=utf8
# 题目: 逆转链表的值(分别采用递归和非递归方式)
# 思路: 先记录下当前节点的下一个节点,然后将当前指针指向前一个节点,再递归处理下一个节点

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverseList(self, head):

        def reverse(head,last):
            if head == None:
                return last
            next = head.next
            head.next = last
            return reverse(next, head)
        return reverse(head, None)

    # 非递归方法
    def reverseList_none_recursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        last = None
        dummy = ListNode(0)
        dummy.next = head
        while dummy.next:
            next = dummy.next.next
            dummy.next.next = last
            last = dummy.next
            dummy.next = next
        return last

# root = ListNode(1)
# root.next = ListNode(2)
# print Solution().reverseList(root)
