class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj={i:set() for i in range(len(points))}
        
        for i in range(len(points)):
            x1,y1=points[i]
            for j in range(i+1,len(points)):
                x2,y2=points[j]
                dist=abs(x2-x1) + abs(y2-y1)
                adj[i].add((dist,j))
                adj[j].add((dist,i))
        
        minheap=[(0,0)] # (cost: point)
        visit,cost=set(),0
        
        while len(visit) < len(points):
            dist,i=heapq.heappop(minheap)
            
            if i in visit:
                continue
            visit.add(i)
            cost+=dist
            
            for path_cost,nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minheap,(path_cost,nei))
            
        return cost
            
        
        
        
        
        
        
        