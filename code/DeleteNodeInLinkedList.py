# coding=utf8
# 题目: 给定链表中的一个节点,从链表中删除这个节点(非尾节点)
# 思路: 讲该节点下一个节点的值复制到当前节点,并将当前节点的指针指向下一个节点的下一个节点

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next