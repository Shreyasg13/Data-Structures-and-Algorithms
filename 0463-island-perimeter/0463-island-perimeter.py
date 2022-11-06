class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit=set()
        
        def DFS(i,j):
            # bound conditions : if edges found
            if i < 0 or i >= len(grid) or j < 0 or j >=len(grid[0]) or grid[i][j]==0:
                return 1
            # IF already visited cell found
            if (i,j) in visit : 
                return 0
            
            visit.add((i,j))
            return DFS(i+1,j)+DFS(i-1,j)+DFS(i,j+1)+DFS(i,j-1)
        
        # Iterating through each and calling DFS on 1s
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    return DFS(r,c)
        return 0
            
            