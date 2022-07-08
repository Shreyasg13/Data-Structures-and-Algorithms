class Solution:
    def topKFrequent(self, nums, k):
        
        Frequency={}
        # Create Frequency Map
        for n in nums:
            if n not in Frequency:
                Frequency[n] = 1
            else :
                Frequency[n]+= 1
                
        container=[] # Min Heap
        # Pushing elements by frequency in min-heap
        for key,val in Frequency.items():
            
            heapq.heappush(container,(val,key))
        # As heap length exceeds k , we will keep on poping least frequent element             
            if len(container) > k:  
                heapq.heappop(container)
                
        ans= [y for x,y in container[::-1]]
        return ans        
            
            
            
            
            
        
        