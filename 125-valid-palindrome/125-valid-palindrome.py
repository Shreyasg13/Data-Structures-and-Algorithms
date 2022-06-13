class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        
        while l < r :
            
            if not self.alphaNumeric(s[l]):
                l+=1
                continue
            if not self.alphaNumeric(s[r]):
                r-=1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l,r=l+1,r-1
        
        return True
    
    def alphaNumeric(self,c):
        return ord('A')<= ord(c)<=ord('Z') or ord('a')<= ord(c)<=ord('z') or ord('0')<= ord(c)<=ord('9')
                
       
        
        
        

        #  s = s.lower()
        # s = re.sub('\W+','',s)
        # return s==s[::-1]