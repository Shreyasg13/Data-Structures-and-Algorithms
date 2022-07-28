class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l=0
        string=set()
        res=0
        # iterrating right pointer
        for r in range(len(s)):
           
            # keep going to next char till duplicate not found
            while s[r] in string:
                string.remove(s[l])
                l+=1
            # keep adding each character of right pointer
            string.add(s[r])
            # print(string)
            res=max(res,len(string))
        return res
