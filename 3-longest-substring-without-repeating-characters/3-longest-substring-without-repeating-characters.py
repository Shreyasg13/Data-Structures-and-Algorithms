class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left=0
        Set=set()
        res=0
        # kepp iterrating each char
        for char in s:
           
            # keep on removing char from set till duplicate found
            while char in Set:
                Set.remove(s[left])
                left+=1
            # keep adding each character of to get subtring 
            Set.add(char)
            # print(string)
            res=max(res,len(Set))
        return res
