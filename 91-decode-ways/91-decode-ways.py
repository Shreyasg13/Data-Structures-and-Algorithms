class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[0]*(len(s)+1)
        dp[0],dp[1]=1,1
        # dp[1,1,n1,n2...n+1]
        if s[0]=="0":
            return 0
        # Top Down approach
        for i in range(2,len(s)+1,1):
            # checking for one digit valid case and add 
            if 1 <= int(s[i-1]) <=9 :
                dp[i]+=dp[i-1]
            # checking for two digit valid case and add 
            if 10<=int(s[i-2]+s[i-1])<=26:
                dp[i]+=dp[i-2]
            
        return dp[-1]
        
        