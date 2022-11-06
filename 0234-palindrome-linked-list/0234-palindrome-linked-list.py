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
            sec=sec.next
            sec=sec.next
            fir=fir.next
            
            
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
            
            
        
#             node2=head
#             node=head
            
#             def rev(node):
#                 prev,cur=None,node
                
#                 while cur:
#                     nxt=cur.next
#                     cur.next=prev
#                     prev=cur
#                     cur=nxt
#                 return prev
#             head2=rev(node)
#             print(head)
#             while head and head2 :
#                 if head.val != head2.val:
#                     return False
                
#                 return True
            
    
#         first=second=node=head
#         l1=0
#         while first and second:
#             l1+=1
#             first=first.next
#             second=second.next.next
            
#         tmp=mid=first
#         print()
#         first.next=None
        
#         while tmp :
#             tmp=tmp.next
#             l1-=1
#         if l1 !=0 :
#             mid=mid.next
#         print(mid,first)
#         return mid==first
            
        
        
        
        
            
            
        