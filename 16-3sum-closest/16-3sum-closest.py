class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=nums[0]+nums[1]+nums[2]
        
        for i in range(len(nums)-2):
  
            l,r=i+1,len(nums)-1
            
            while l < r:
                s=nums[l]+nums[r]+nums[i]
            # if close sum found the store in in res               
                if abs(s-target) < abs(res-target):
                    res=s
            # shift poiters on the basis of current sum        
                if s > target:
                    r-=1
                elif s < target:
                    l+=1
            # break early in taget found
                else:
                     return res 
        return res        
       
       