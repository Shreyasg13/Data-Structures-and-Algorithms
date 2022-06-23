class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sqrt=[]
        res=[]
        for i in range(len(points)):
            print(i)
            sqrt.append([-1*(points[i][0]**2 + points[i][1]**2),i])
              
            
        heapq.heapify(sqrt)
        print(sqrt)

        while len(sqrt) > k :
            heapq.heappop(sqrt)
        
        for [x,y] in sqrt:
            res.append(points[y])
        
        return res
            
        
        