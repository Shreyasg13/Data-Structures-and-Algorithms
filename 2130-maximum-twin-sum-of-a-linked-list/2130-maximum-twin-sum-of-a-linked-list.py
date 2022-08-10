# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=ListNode(0,head)
        fast=head
		#Finding The Mid Node of the LL
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
		#Reversing the second half of Linked List
        slow.next=prev=None
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        first,second=head,prev
        res=0
		#Adding the corresponding parts of the 2 divided linked list
        while first:
            res=max(res,first.val+second.val)
            first=first.next
            second=second.next
        return res