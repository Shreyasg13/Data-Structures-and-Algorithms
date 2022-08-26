class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows,cols=len(grid),len(grid[0])
        visited=set()
        def DFS(r,c):
            
            if (r >= rows or r < 0 or c >= cols or c < 0
            or grid[r][c]=="0" or (r,c) in visited):
                return
            
            visited.add((r,c))
            
            DFS(r,c+1)
            DFS(r,c-1)
            DFS(r+1,c)
            DFS(r-1,c)
            
        count=0    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    count+=1
                    DFS(r,c)
        return count
        