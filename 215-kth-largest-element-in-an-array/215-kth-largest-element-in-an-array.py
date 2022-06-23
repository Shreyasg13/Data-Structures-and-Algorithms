class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr=[-ele for ele in nums]
        heapq.heapify(arr)
        
        while k !=1 :
            k-=1
            heapq.heappop(arr)
        
        return-heapq.heappop(arr)
        
        