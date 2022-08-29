class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create an adjuscency list
        pre=[[] for _ in range(numCourses)]
        for x,y in prerequisites: pre[x].append(y)
        
        Visited,Taken=set(),[]
        
        def DFS(crs):
            
            if crs in  Visited:
                return False
            if crs in Taken :
                return True
           # add crs then check its all prereqs and remove that course 
            Visited.add(crs)
            
            for p in pre[crs]:
                if DFS(p)==False:
                    return False
            
            Visited.remove(crs)
            Taken.append(crs)
            
        for i in range(numCourses):
            if DFS(i)==False:
                return []
        return Taken
            
            