# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find mid 
        one,two=head,head.next
        
        while two and two.next:
            one=one.next
            two=two.next.next
        
        sec=one.next
        prev=one.next=None #end of first list

        while sec:
            nxt=sec.next
            sec.next=prev
            prev=sec
            sec=nxt
            
        # merging the two list
        
        fir,sec=head,prev
        
        while sec:
            tmp1,tmp2=fir.next,sec.next
            fir.next=sec
            sec.next=tmp1
            fir,sec=tmp1,tmp2
        
        
        """
        Do not return anything, modify head in-place instead.
        """
        