class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(city):
            visit.add(city)
            
            for endcity in range(len(M)):
                if M[city][endcity]==1 and endcity not in visit:
                    dfs(endcity)
            
        total=0
        visit=set()
        
        for city in range(len(M)):
            if city not in visit:
                total+=1
                dfs(city)
        return total
        