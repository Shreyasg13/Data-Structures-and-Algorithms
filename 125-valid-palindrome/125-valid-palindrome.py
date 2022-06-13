class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        
        while l < r :
            
            while not self.alphaNumeric(s[l]) and l < r:
                l+=1
            while not self.alphaNumeric(s[r]) and l < r:
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l,r=l+1,r-1
        
        return True
    
    def alphaNumeric(self,c):
        return ord('A')<= ord(c)<=ord('Z') or ord('a')<= ord(c)<=ord('z') or ord('0')<= ord(c)<=ord('9')
                
       
        
        
        

        #  s = s.lower()
        # s = re.sub('\W+','',s)
        # return s==s[::-1]