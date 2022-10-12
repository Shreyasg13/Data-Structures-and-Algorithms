class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left,right=0,0
        # keep on checking throught the lengths of strings
        while left < len(s) and right < len(t):
            # if equals push both pointers forward
            if s[left]==t[right]:
                left+=1
                right+=1
            # keep on pushing sencond pointer till end 
            else:
                right+=1
                
        return True if left==len(s) else False