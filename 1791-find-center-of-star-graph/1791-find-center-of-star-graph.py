class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first=edges[0][0]
        second=edges[0][1]
        return first if first in edges[1] else second
            
        