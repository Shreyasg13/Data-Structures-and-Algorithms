# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = ListNode()
        dummy,carry=cur,0
        
        while l1 or l2 or carry :
            # setting digit val
            d1,d2=l1.val if l1 else 0,l2.val if l2 else 0
            # calculate new digit
            
            digit=d1+d2+carry
            carry=digit//10
            digit=digit%10
            cur.next=ListNode(digit)
            
            # shift pointers next elements
            l1,l2,cur=l1.next if l1 else None,l2.next if l2 else None,cur.next
            
        return dummy.next
            