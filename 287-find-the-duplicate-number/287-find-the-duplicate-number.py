class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
#         hash=set()
        
#         for ele in nums:
            
#             if ele in hash:
#                 return ele
#             else:
#                 hash.add(ele)


        while nums[nums[0]]!=nums[0]:
            nums[nums[0]],nums[0]=nums[0],nums[nums[0]]
        return nums[0]
        