import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        Map={}
        MinHeap=[]
        for ele in nums:
            if ele not in Map:
                Map[ele]=-1
            else:
                Map[ele]-=1
        print(Map)
        
        for key,val in Map.items():
            heapq.heappush(MinHeap,[val,key])
        heapq.heapify(MinHeap)
        print(MinHeap)
        
        res=[]
        for i in range(k):
            val,key=heapq.heappop(MinHeap)
            res.append(key)
            
        return res
            
        