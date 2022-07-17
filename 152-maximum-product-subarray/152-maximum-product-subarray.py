class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        prod=1
        Cur_Max,Cur_Min=1,1
        for n in nums:
            if  n == 0:
                Cur_Min=1
                Cur_Max=1
                continue
            
            Cur_Max,Cur_Min=max(Cur_Max*n,Cur_Min*n,n ),min(Cur_Max*n,Cur_Min*n,n )
            res=max(Cur_Max,res)
        return res