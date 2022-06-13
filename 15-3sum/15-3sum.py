class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet=[]
        nums.sort()
        for i, ele in enumerate(nums):
            if i > 0 and ele==nums[i-1]:
                continue
            
            l,r=i+1,len(nums)-1
            while l < r:
                Sum=nums[l]+nums[r]+ele
            
                if  Sum > 0:
                    r-=1
                elif Sum < 0:
                    l+=1
                else:
                    triplet.append([ele,nums[l],nums[r]])
                    l+=1
            
                    while nums[l]==nums[l-1] and l < r  :
                        l+=1
                        
                        
        return triplet 
            
                
        