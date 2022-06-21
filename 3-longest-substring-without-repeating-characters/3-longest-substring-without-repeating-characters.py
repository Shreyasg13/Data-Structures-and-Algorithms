class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l=0
        string=set()
        res=0
        for r in range(len(s)):
            while s[r] in string:
                string.remove(s[l])
                l+=1
            string.add(s[r])
            res=max(res,r-l+1)
        return res
        
        
        
#         charSet = set()
#         l = 0
#         res = 0
        
#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             res = max(res, r - l + 1)
#         return res