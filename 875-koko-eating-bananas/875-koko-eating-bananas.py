class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r=1,max(piles)
        
        res=r
        while l <= r:
            k=(l+r)//2
            hours=0
            for p in piles:
                hours+=math.ceil(p/k)
            
            if hours <= h :
                r=k-1
                res=min(res,k)
            else:
                l=k+1
        return res
                
                
             
       
            
#         k = 1
#         while True:
#             total_time = 0
#             for i in piles:
#                 total_time += ceil(i / k)
#             if total_time > h:
#                 k += 1
#             else:
#                 return k
        