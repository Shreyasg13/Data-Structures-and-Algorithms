# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy=ListNode(0,head)
        l,r=head,head
        # take a pointer to n
        for i in range(n):
            r=r.next
        if not r: return head.next
        # reach till end
        while r.next:
            l,r = l.next,r.next
        # delete node
        
        l.next=l.next.next
        
        return head