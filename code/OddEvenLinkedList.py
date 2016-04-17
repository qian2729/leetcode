# coding=utf8
# 题目: 给定一个链表,将链表奇数位置的值放在链表最前面,偶数位置的值放置在链表最后面
# 思路: 利用两个头指针,一个指向奇数位置的节点组成的链表,一个指向偶数位置的节点组成的链表.遍历源链表的时候每次移动两个位置,分别将
# 奇数位置和偶数位置的节点加入相应的链表中, 最后将新得到的奇数位置的链表的末尾节点指向偶数位置链表的头节点.

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        oddHead = head
        evenHead = head.next
        odd = oddHead
        even = evenHead
        head = head.next
        while head.next:
            odd.next = head.next
            odd = odd.next
            head = head.next
            if head.next:
                even.next = head.next
                even = even.next
                head = head.next
        odd.next = evenHead
        even.next = None
        return oddHead
