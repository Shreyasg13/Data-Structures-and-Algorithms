class Solution:

        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Create connected graph
        Graph={}
        for x,y in edges:
            if x not in Graph:
                Graph[x]=[]
            if y not in Graph:
                Graph[y]=[]
            Graph[x].append(y)
            Graph[y].append(x)
            
        # print(Graph)  
        
        
        def dfs(src,dest,Graph,visited):
            
            if src==dest: return True
            if src in visited: return False
            visited.add(src)
            # check into its neighbours recursively
            for nei in Graph[src]:
                if dfs(nei,dest,Graph,visited)==True:
                    return True
            return False
    
        return dfs(source,destination,Graph,set())
            
            
            
            
            
        