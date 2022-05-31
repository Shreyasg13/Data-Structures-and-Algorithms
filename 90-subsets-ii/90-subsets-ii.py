class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):
        if path not in res:
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)
    
        

        