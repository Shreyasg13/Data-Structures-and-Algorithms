class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        great,small=float('inf'),float('-inf')
        for i in range(len(nums)-2):
            
            if i > 0 and nums[i]==nums[i-1]:
                continue
            
            l,r=i+1,len(nums)-1
            
            while l < r:
                s=nums[l]+nums[r]+nums[i]
                if s==target:
                    return target
                if s > target:
                    r-=1
                    great=min(great,s)
                else:
                    l+=1
                    small=max(small,s)
        if  abs(great-target)> abs(small-target):
            return small
        else:
            return great
       