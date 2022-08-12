# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l,r=head,head
        
        # setting left pointer on kth node from begining
        for i in range(k-1):
            r=r.next
        
        first=r
        
        # setting right pointer on kth node from end
        while r.next:
            l,r = l.next,r.next
        
        second=l
        
        # Swap Node Values
        first.val,second.val=second.val,first.val

        
        return head
        
        
        
        