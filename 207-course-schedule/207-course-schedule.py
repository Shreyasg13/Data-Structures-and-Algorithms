class Solution:
    def canFinish(self, N, edges):
        # Create a map of crs and their repective prereqs
        adj_list=[[] for i in range(N)]
        for x,y in edges: adj_list[x].append(y)
        
        
        """
    # Implement DFS for each course
        1.Maintain the visit set
        2. if the course you selected 
            I.add crs in visit set and check for its prereqs
            II. Its in visited set i.e. you found a cycle
            III. If its empty i.e. its prerequisites are taken already and can truen True
        3. call the DFS function on all number of courses
        """
        visit=set()
        def DFS(crs):
            
            if crs in visit:
                return False
            if adj_list[crs]==[]:
                return True
            
            visit.add(crs)
            for nei in adj_list[crs]:
                
                if not DFS(nei):
                    return False
            visit.remove(crs)
            adj_list[crs]=[]
            return True
            
        for crs in range(N):
            if not DFS(crs):
                return False
        return True
            
        