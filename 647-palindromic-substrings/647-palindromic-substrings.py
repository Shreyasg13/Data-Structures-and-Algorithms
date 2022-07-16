class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            # check even pallindrome
            tmp=self.helper(s,i,i+1)
            if tmp > 0:
                count+=tmp
            tmp=self.helper(s,i,i)
            if tmp > 0:
                count+=tmp
        return count
        
    def helper(self,s,l,r):
        n=0
        while l>=0 and r <len(s) and s[l]==s[r]:
            n+=1
            l-=1
            r+=1
        return n
        