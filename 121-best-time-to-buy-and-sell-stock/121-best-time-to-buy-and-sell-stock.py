class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        profit=0
        l=0
        for r in range(1,len(prices)):
            if prices[l] < prices[r]:
                profit=max(prices[r]-prices[l],profit)
            else:
                l=r
        return profit
#         l,r,profit=0,1,0
#         while r <len(prices):
#             if prices[l] < prices[r]:
#                 profit=max(prices[r] -prices[l],profit)
#             else:
#                 l=r
#             r+=1
#         return profit
                            
                       

        