# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ans=ListNode()
        ans.next=list1
        
        # If both Nodes present order them decresing 
        while list1 and list2:
            
            if list1.val < list2.val:
                ans.next=list1
                list1=list1.next
                
            else:
                ans.next=list2
                list2=list2.next
                
            ans=ans.next
        
        # For handling single Node present 
        if list1 and not list2:
            ans.next=list1
        elif not list1 and list2:
            ans.next=list2
       
        return head.next
            
        
        
        
        
#         # Recursive
#         if not list1 or not list2:
#             return list1 or list2
        
#         if list1.val < list2.val:
#             list1.next=self.mergeTwoLists(list1.next,list2)
#             return list1
#         else:
#             list2.next=self.mergeTwoLists(list1,list2.next)
#             return list2
          
            
#             # Iterative
#         dummy = res = ListNode()
#         # res.next=list1.val
#         while list1 and list2:    
#             if list1.val <list2.val:
#                 res.next=list1
#                 list1=list1.next
#             else:
#                 res.next=list2
#                 list2=list2.next
                
#             res=res.next
#         res.next=list1 or list2
#         return dummy.next
        
            
            
        
        
        