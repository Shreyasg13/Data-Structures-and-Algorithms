class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        hash=set()
        
        for ele in nums:
            
            if ele in hash:
                return ele
            else:
                hash.add(ele)