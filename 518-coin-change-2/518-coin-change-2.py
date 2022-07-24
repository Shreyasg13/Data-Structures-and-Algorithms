class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for a in range(1, amount + 1):
                # if amount is left or equals keep on adding 
                if a - coin >= 0:
                    dp[a] += dp[a - coin]
        print(dp)
        return dp[-1]