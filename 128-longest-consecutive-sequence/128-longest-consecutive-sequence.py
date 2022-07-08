class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        A=set(nums)
        ans=0
     
        for ele in A:
            # if prev sequence doest exist
            # Iternate till last element avilable in list
            if (ele-1) not in A:
                last=ele+1
                while last in A:
                    last+=1
                ans=max(last-ele,ans)
            
        return ans
                
                
        
        
      
                    
            
                
                
        