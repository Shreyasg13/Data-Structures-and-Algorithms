"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        Map={None:None}
        
        cur=head
        # creating a copy in hashmap with constructer
        while cur:
            copy=Node(cur.val)
            Map[cur]=copy
            cur=cur.next
        
        cur=head
        # setting next and random for copy and simply return the head pointer from hashmap
        while cur:
            copy=Map[cur]
            copy.next   =   Map[cur.next]
            copy.random =   Map[cur.random]
            cur=cur.next
        
        return Map[head]