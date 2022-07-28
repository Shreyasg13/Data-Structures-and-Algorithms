class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left=0
        Set=set()
        res=0
        
        for char in s:
           
            # keep going to next char till duplicate not found
            while char in Set:
                Set.remove(s[left])
                left+=1
            # keep adding each character of right pointer
            Set.add(char)
            # print(string)
            res=max(res,len(Set))
        return res
