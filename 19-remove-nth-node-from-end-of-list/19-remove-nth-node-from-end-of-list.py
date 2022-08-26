# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l,r=head,head
        
        for _ in range(n):
            r=r.next
        if not r:
            head=head.next
            return head
        while r.next:
            r=r.next
            l=l.next
        
        l.next=l.next.next
        return head
        
        
        
        
        
        
#         l,r=head,head
#         # reach till the Nth Node 
#         for i in range(n):
#             r=r.next
        
#         # if right pointer gets beyond list 
#         # It implies that we have to remove last node 
        
#         if not r:
#             head= head.next
#             return head
        
#         # Keep dragging a window till end# reach till the Nth Node 
#         while r.next:
#             r=r.next
#             l=l.next
#         # Left will be now at Nth Node
        
#         l.next=l.next.next
        
#         return head
        
        