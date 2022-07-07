class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adj=defaultdict(set)
        
        
        def dfs(u,v): #Measures if s and d CAN be connected directly or indirectly.
            if u in visited:
                return False
            if u==v:
                return True
            
            visited.add(u)
            for i in adj[u]:
                if dfs(i,v):
                    return True
            return False
                
                
        
        for x,y in edges: 
            
            visited=set()
            if dfs(x,y):
                return [x,y]
            
            adj[x].add(y)
            adj[y].add(x)
            
        
            
            
      
               
        