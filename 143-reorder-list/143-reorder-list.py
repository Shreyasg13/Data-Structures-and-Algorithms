# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
         # Finding a  mid and making first half and second half
        slow,fast=head,head.next
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        fir=head
        sec=slow.next
        slow.next=None
        
        # Reversing the second half
        prev=None
        
        while sec:
            tmp=sec.next
            sec.next=prev
            prev=sec
            sec=tmp
        
        fir,sec=head,prev
        
      
        
        while fir and sec:
            tmp1,tmp2=fir.next,sec.next
            fir.next=sec
            sec.next=tmp1
            
            fir,sec=tmp1,tmp2
        
        
        """
        Do not return anything, modify head in-place instead.
        """