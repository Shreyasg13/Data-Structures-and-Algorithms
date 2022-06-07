class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        D1,D2={},{}
        
        for i in range(len(s)):    
            D1[s[i]]=1+D1.get(s[i],0)
            D2[t[i]]=1+D2.get(t[i],0)
        for i in range(len(s)):
            if D1[s[i]] != D2.get(s[i],0):
                    return False
        return True
                    
               
             
               
        
               
                
               
            
           