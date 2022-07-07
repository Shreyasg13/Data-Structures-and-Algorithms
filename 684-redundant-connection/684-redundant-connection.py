class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adj=defaultdict(set)
        
        
        def dfs(s,d): #Measures if s and d CAN be connected directly or indirectly.
            if s not in visit:
                visit.add(s)
                if s==d:
                    return True
                return any(dfs(i,d) for i in adj[s])
            return False
        
        
        for x,y in edges: 
            visit=set()
            if dfs(x,y):
                return [x,y]
            adj[x].add(y)
            adj[y].add(x)
            
        
            
            
      
               
        