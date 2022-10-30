class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        leftsum=0
        
        for i in range(len(nums)):
            # checking if leftsum is equals rightsum
            if leftsum==total-nums[i]-leftsum:
                return i
            # update leftsum at index i
            leftsum+=nums[i]
        return -1