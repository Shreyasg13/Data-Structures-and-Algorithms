class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dict={}
        for i in range (len(nums)):
            num2=target-nums[i]
            if  num2 not in Dict :
                Dict[nums[i]]=i
            else:
                return[Dict[num2],i]
                
            
        
