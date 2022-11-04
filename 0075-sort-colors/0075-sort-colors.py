class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            tmp=nums[i]
            nums[i]=nums[j]
            nums[j]=tmp
            
        l,r=0,len(nums)-1
        i=0
        while i <= r :
            
            if nums[i]==0:
                # swap l with i
                # nums[i],nums[l]=nums[l],nums[i]
                swap(l,i)
                l+=1
            elif nums[i]==2:
                # swap i with r 
                # nums[i],nums[r]=nums[l],nums[r]
                swap(i,r)
                r-=1
                i-=1
            i+=1
        