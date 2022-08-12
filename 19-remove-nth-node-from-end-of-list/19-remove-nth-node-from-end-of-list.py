# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        l,r=head,head
        
        for i in range(n):
            r=r.next
        # if right pointer gets beyond list 
        if not r:
            head= head.next
            return head
        
        
        while r.next:
            r=r.next
            l=l.next
        
        l.next=l.next.next
        
        return head
        
        