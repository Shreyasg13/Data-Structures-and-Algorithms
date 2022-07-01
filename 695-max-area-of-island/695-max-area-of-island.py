class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        max_island = 0
        visited=set()
        
        def dfs(r,c, visited):
            if ( r not in range(rows)
                or c not in range(cols) or
                grid[r][c]==0) or (r,c) in visited :
                return 0
            
            
            if grid[r][c]==1:
                visited.add((r,c))
                
                up = dfs(r-1,c,visited)
                down = dfs(r+1,c,visited)
                left = dfs(r,c-1,visited)
                right = dfs(r,c+1,visited)
                        
            return 1 + up + down + left + right
                
            
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    curr_area = dfs(r,c,visited)
                
                    max_island = max(max_island,curr_area)
           
        return max_island
                
                
        