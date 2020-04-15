from math import ceil;
import heapq;
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        rhead = ListNode(-1);
        rtail = rhead; 
        nc = 0 ; # count;         
        for i in range(len(lists)): 
            if (lists[i] != None):
                heapq.heappush(heap, lists[i].val)
                lists[i] = lists[i].next;        
        #print(("init heap", heap));        
        while nc != len(lists):
            nc = 0
            for i in range(len(lists)): 
                if (lists[i] != None):
                    #print((i, lists[i].val))                
                    if len(heap) > 0: 
                        while (lists[i] != None and lists[i].val <= heap[0]) :
                            rtail.next = ListNode(lists[i].val)
                            rtail = rtail.next
                            lists[i] = lists[i].next
                            #print(("result", printList(rhead.next)));
                    if (lists[i] != None):                        
                        heapq.heappush(heap, lists[i].val)
                        #print(heap)
                        lists[i] = lists[i].next;
            if (len(heap) == 0):
                return rhead.next;
            rtail.next = ListNode(heapq.heappop(heap))
            rtail = rtail.next   
