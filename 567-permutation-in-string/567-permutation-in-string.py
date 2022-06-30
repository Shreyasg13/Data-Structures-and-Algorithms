class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        len1,len2=len(s1),len(s2)
        
        hash1=[0]*26
        hash2=[0]*26
                
        
                
        for c in s1:
            hash1[ord(c)-ord('a')]+=1
            
        for i in range(len2):
            
            if i < len1:
                hash2[ord(s2[i])-ord('a')]+=1
            else:
                hash2[ord(s2[i])-ord('a')]+=1
                hash2[ord(s2[i-len1])-ord('a')]-=1
            if hash1==hash2:
                return True
    
        return False
    
                
        

            