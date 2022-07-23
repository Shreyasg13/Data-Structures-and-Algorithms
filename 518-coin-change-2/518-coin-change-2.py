class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache={}
        def dfs(i,a):
            
            if amount < a or i==len(coins):
                return 0
            
            if amount == a:
                return 1
            
            if (i,a) in cache:
                return cache[(i,a)]
            
            cache[(i,a)]= dfs(i,a+coins[i]) + dfs(i+1,a)
            return cache[(i,a)]    
        return dfs(0,0)
