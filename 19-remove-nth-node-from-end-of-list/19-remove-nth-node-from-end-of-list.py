# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left,right=head,head
        
        # reach till the Nth Node 
        for _ in range(n):
            right=right.next
        
        if not right:
            return head.next
            
        # keep dragging windown till end 
        
        while right.next:
            left,right=left.next,right.next
            
        # i.e. left will be now at N th Node 
        
        left.next=left.next.next
        
        return head
        
        