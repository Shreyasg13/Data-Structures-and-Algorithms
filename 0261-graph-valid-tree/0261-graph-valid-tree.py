class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n-1 :
            return False
        
        adj={i:[] for i in range(n)}
        
        for x,y in edges :
            adj[x].append(y)
            adj[y].append(x)
        
        visit=set()
        
        def dfs(i):
            visit.add(i)
            for neigh in adj[i]:
                if neigh not in visit:
                    dfs(neigh)
        dfs(0)
        
        return len(visit)==n
        
        
        
    """ Iterative Solution"""
#         stack=[0]
#         while stack:
#             node=stack.pop()
#             visit.add(node)
            
#             for nei in adj[node]:
#                 if nei not in visit:
#                     stack.append(nei)
#         return len(visit)==n
            
        
      