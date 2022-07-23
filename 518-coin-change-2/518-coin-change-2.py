class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for i in range(len(coins) - 1, -1, -1):
            # creating temporory memory
            new_dp = [0] * (amount + 1)
            new_dp[0] = 1

            for a in range(1, amount + 1):
                new_dp[a] = dp[a]
                # if amount is left or equals keep on adding 
                if a - coins[i] >= 0:
                    new_dp[a] += new_dp[a - coins[i]]
            # re-assign values to dp
            dp = new_dp
        return dp[amount]