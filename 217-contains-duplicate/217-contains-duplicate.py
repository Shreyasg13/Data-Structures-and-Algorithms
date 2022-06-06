class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Map=set()
        for i in nums:
            if i in Map:
                return True
            Map.add(i)
        return False