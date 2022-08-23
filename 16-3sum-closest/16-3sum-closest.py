class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
  
            l,r=i+1,len(nums)-1
            
            while l < r:
                s=nums[l]+nums[r]+nums[i]
                
                if abs(s-target) < abs(res-target):
                    res=s
                if s > target:
                    r-=1
                elif s < target:
                    l+=1
                else:
                    return res
        return res        
       
       