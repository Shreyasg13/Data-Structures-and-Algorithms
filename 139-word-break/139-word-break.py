class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
       
        Mark=[False]*(len(s)+1)
        Mark[len(s)]=True
        
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if (len(word)+i)<=len(s) and s[i:i+len(word)] == word and Mark[i+len(word)]:
                    Mark[i]=True
                    break
        
        return Mark[0]