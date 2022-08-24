class Solution:
    def firstUniqChar(self, s: str) -> int:
  
        Dict={}
        for i in range(len(s)):
            if s[i] not in Dict:
                Dict[s[i]]=1
            else:
                Dict[s[i]]+=1
        
        for i in range(len(s)):
            if Dict[s[i]]==1:
                return i
        return -1
        