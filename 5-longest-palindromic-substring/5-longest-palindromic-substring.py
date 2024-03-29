class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=""
        
        for i in range(len(s)):
            # checking for odd pal seq
            tmp=self.Pallindrome(s,i,i)
            if len(tmp) > len(longest):
                longest=tmp
            # checking for even pal seq
            tmp=self.Pallindrome(s,i,i+1)
            if len(tmp) > len(longest):
                longest=tmp
        return longest
    # get longest pallindrome at index i       
    def Pallindrome(self,s,l,r):
        while l>=0 and r<=len(s)-1 and s[r]==s[l]:
            l-=1
            r+=1
        return s[l+1:r]
        
    
        
        