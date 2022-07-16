class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            # check even pallindrome
            tmp=self.Num_of_pallindromes(s,i,i+1)
            if tmp > 0:
                count+=tmp
                
            # check even pallindrome
            tmp=self.Num_of_pallindromes(s,i,i)
            if tmp > 0:
                count+=tmp
        return count
    # Calculating pallindromes at index i
    def Num_of_pallindromes(self,s,l,r):
        n=0
        while l>=0 and r <len(s) and s[l]==s[r]:
            n+=1
            l-=1
            r+=1
        return n
        