# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy=curr=ListNode(0)
        heap=[]
        for i in range(len(lists)):
        # maintain the index,val of first element of lists  
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i))
                lists[i]=lists[i].next
                
        # print(heap)
        while heap:
            # pop lowest element & add next element of i'th list in heap
            val,i=heapq.heappop(heap)
            curr.next=ListNode(val)
            curr=curr.next
             
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i))
                lists[i]=lists[i].next
            # print(heap)
        return dummy.next
                
                
        