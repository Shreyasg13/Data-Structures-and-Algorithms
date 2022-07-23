class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Intialize 2D array 
        dp  =   [[0 for _ in range(len(coins)+1)] for _ in range(amount+1)]
        dp[0] = [1] * (len(coins) + 1)
        # Bottom up approach 
        
        for a in range(1,amount+1):
            for i in range (len(coins)-1,-1,-1):
            
            # checking number of ways the coin can sum to amount 
                dp[a][i]=dp[a][i+1]
                if a-coins[i] >=0:
                    dp[a][i]+=dp[a-coins[i]][i]
        # returning the ways we can sum upto amount
        return dp[amount][0]