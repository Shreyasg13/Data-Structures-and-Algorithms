class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache={}
        
        def dfs(i,buying):

            if i >= len(prices):
                return 0
            if (i,buying) in cache:
                return cache[(i,buying)]
            # curr cooldown value
            cool=dfs(i+1,buying)
            
            if buying:
                # buying and decrementring profit with caching max profit at value i
                buy= dfs(i+1,not buying)-prices[i]
                cache[(i,buying)]=max(cool,buy)
            else:
                # selling and incremented profit with caching max profit at value i
                sell=dfs(i+2,not buying) + prices[i]
                
                cache[(i,buying)]=max(sell,cool)
            return cache[(i,buying)]
        
        return dfs(0,True)
            
            