class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,profit=0,1,0
        while r <len(prices):
            if prices[l] < prices[r]:
                profit=max(prices[r] -prices[l],profit)
            else:
                l=r
            r+=1
        return profit
                            
                       

        