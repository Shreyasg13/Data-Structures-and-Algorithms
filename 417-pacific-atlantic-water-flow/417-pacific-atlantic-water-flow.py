class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        row,col=len(heights),len(heights[0])
        pac,alt=set(),set()
        
        def dfs(r,c,visit,prev_height):
            if ((r,c) in visit or 
               r<0 or r >=row or 
               c<0 or c >=col or heights[r][c] < prev_height):
                return
            
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            
            
        
        for c in range(col):
            dfs(0,c,pac,heights[0][c])
            dfs(row-1,c,alt,heights[row-1][c])
            
        for r in range(row):
            dfs(r,0,pac,heights[r][0])
            dfs(r,col-1,alt,heights[r][col-1])
            
        points=[]
        for r in range(row):
            for c in range(col):
                if (r,c) in pac and (r,c) in alt:
                    points.append([r,c])
                    
        return points
            
        
            
        
        
        
        