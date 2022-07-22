class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1,len2=len(text1)+1,len(text2)+1
        dp=[[0 for j in range(len2)] for i in range(len1)]
        # bottom up approach
        
        for i in range(len1-2,-1,-1):
            for j in range(len2-2,-1,-1):
                # if element found
                if text1[i]==text2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                # storing previous longest subsequence
                else:
                    dp[i][j]=max( dp[i+1][j] , dp[i][j+1] )
        return dp[0][0]
        
      