class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        D1,D2={},{}
        
        for i in range(len(s)):    
            D1[s[i]]=1+D1.get(s[i],0)
            D2[t[i]]=1+D2.get(t[i],0)
        for ele in D1:
            if D1[ele] != D2.get(ele,0):
                    return False
        return True
                    
               
             
               
        
               
                
               
            
           