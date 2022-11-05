# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fir=head
        sec=head
        # Find middle
        while sec and sec.next:
            
            fir=fir.next
            sec=sec.next
            sec=sec.next
            
        prev=None
        # reverse next half
        while fir :
            tmp= fir.next
            fir.next=prev
            prev=fir
            fir=tmp
        
        left,right=head,prev
        
        while right:
            if left.val != right.val :
                return False
            left=left.next
            right=right.next
        return True
            
 