class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        Max=[1,1,1]
        for t in triplets:
            if t[0] <=target[0] and t[1] <= target[1] and t[2] <= target[2] :
                Max[0]=max(Max[0],t[0])
                Max[1]=max(Max[1],t[1])
                Max[2]=max(Max[2],t[2])
            if Max==target:
                return True
        return False
            
