class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre={i:[] for i in range(numCourses)}
        
        for x,y in prerequisites:
            pre[x].append(y)
        cycle,taken=set(),[]
        def CanTake(crs):
            
            if crs in cycle:
                return False
            if crs in taken:
                return True  
            
            cycle.add(crs)
            for ele in pre[crs]:
                if CanTake(ele)==False:
                    return False    
            
            cycle.remove(crs)
            taken.append(crs)
            
            
            
        for i in range(numCourses):
            if CanTake(i)==False:
                return []
                
        return taken
                
        