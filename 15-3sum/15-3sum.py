class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            
            if i > 0 and nums[i]==nums[i-1]:
                continue
            
            l,r=i+1,len(nums)-1
            mid=(l+r)//2
            while l < r:
            
                sum=nums[i]+nums[l]+nums[r]
            
                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l < r and nums[l]==nums[l-1]:
                        l+=1
                            
                    
        return res
    
    
    
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         triplet=[]
#         nums.sort()
#         for i, ele in enumerate(nums):
#             if i > 0 and ele==nums[i-1]:
#                 continue
            
#             l,r=i+1,len(nums)-1
#             while l < r:
#                 Sum=nums[l]+nums[r]+ele
            
#                 if  Sum > 0:
#                     r-=1
#                 elif Sum < 0:
#                     l+=1
#                 else:
#                     triplet.append([ele,nums[l],nums[r]])
#                     l+=1
            
#                     while nums[l]==nums[l-1] and l < r  :
#                         l+=1
                        
                        
#         return triplet