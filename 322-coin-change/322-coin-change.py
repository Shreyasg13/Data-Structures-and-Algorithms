class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [sys.maxsize for _ in range(amount)]
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        if dp[amount] == sys.maxsize:
            return -1
        return dp[amount]
            
        
        
#         coins.sort()
#         print(coins[len(coins)-1])
#         if coins[len(coins)-1] > amount:
#             return -1
#         # amount=0
#         count=0
#         for i in range(len(coins)-1,-1,-1):
#             if coins[i] > amount:
#                 pass
#             else:
#                 count+=amount//coins[i]
#                 amount%=coins[i]
#                 print(count,amount)
#             # if rem amount is less than coin
#             if amount //coin[i]:
#                 return -1
#             if amount==0:
#                 return count
        
            
#         return count
        
        