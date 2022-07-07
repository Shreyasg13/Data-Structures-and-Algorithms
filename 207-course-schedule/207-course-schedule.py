class Solution:
    def canFinish(self, N, edges):
        Adj_List = [[] for _ in range(N)]
        status = [0 for _ in range(N)]
        for x,y in edges: Adj_List[x].append(y)
        
        def dfs(crs):
            # if came across visited course
            if status[crs]==1:
                return True
            # already visited course
            if status[crs]==-1:
                return False
            status[crs]= -1
            
            for pre in Adj_List[crs]:
                
                if not dfs(pre):
                    return False
            
            status[crs]=1
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


        
        