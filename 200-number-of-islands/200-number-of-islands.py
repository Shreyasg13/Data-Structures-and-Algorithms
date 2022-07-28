class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        
        rows,cols=len(grid),len(grid[0])
        # pos=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=set()
        
        def dfs(r,c):
            
            if(r>rows-1 or r <0 or c >cols-1 or c <0 
            or (r,c) in visited or grid[r][c]=='0'):
                    return
            visited.add((r,c))
#             for lr,lc in pos:
#                 dfs(r+lr,c+lc)    
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
                
            
            
        total=0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]=='1':
                    total+=1
                    dfs(r,c)
                    
        
        return total
        