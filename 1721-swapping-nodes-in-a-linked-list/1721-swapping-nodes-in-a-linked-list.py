# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l,r=head,head
        # setting up pointer on n from beg and n from end
        for i in range(k-1):
            r=r.next
        
        first=r
        
        while r.next:
            l,r = l.next,r.next
        
        second=l
        print(first.val,second.val)
        
        first.val,second.val=second.val,first.val

        
        return head
        
        
        
        