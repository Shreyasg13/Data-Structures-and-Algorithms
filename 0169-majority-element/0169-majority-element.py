class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map={}
        res,index=0,0
        
        for i in range(len(nums)):
            cur=nums[i]
            if cur not in map:
                map[cur]=1
            else:
                map[cur]+=1
            if max(res,map[cur]) == map[cur]:
                index=i
            if max(res,map[cur]) > len(nums)/2:
                return nums[index]
        return nums[index]
        