class Solution:  
    
    def canFinish(self, N, PreReq):
        graph = {i:[] for i in range(N)}
        status = [0 for i in range(N)]
        for x,y in PreReq:
            graph[x].append(y)
        print(graph)
        
        def dfs(i):
            if status[i] == -1:
                return False
            if status[i] == 1:
                return True
            
            status[i]= -1
            for j in graph[i]:    
                if not dfs(j):
                    return False
            
            status[i]= 1
            return True
        
        for crs in range(N):
            if not dfs(crs):
                return False
        return True
            
            
                
        
            
        
        
#         pre = defaultdict(list)
#         for x, y in edges: pre[x].append(y)

#         status = [0] * N
#         def canTake(i):
#             if status[i] in {1, -1}: return status[i] == 1
#             status[i] = -1
#             if any(not canTake(j) for j in pre[i]): return False
#             status[i] = 1
#             return True

#         return all(canTake(i) for i in range(N))


        
        