# https://leetcode.com/problems/merge-two-sorted-lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1);
        tail = head
        while (l1 != None and l2 != None):
            if (l1.val <= l2.val):
                tail.next = ListNode(l1.val);
                tail = tail.next;
                l1 = l1.next
            else: 
                tail.next = ListNode(l2.val);
                tail = tail.next;
                l2 = l2.next
        if (l1 == None ):
            while (l2 != None):
                tail.next = ListNode(l2.val);
                tail = tail.next;
                l2 = l2.next
        else:
            while (l1 != None):
                    tail.next = ListNode(l1.val);
                    tail = tail.next;
                    l1 = l1.next        
        return head.next
