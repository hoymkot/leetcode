# https://leetcode.com/problems/merge-two-sorted-lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1;
        if (l1.val <= l2.val):
            head = l1
            other = l2
        else:
            head = l2
            other = l1            
        tail = head           
        while other != None:
            if (tail.next == None):
                tail.next = other
                return head            
            if (other.val <= tail.next.val):
                node = other
                other = other.next
                node.next = tail.next
                tail.next = node
            tail = tail.next
            
        return head
