class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        fresh=set()
        rotten=collections.deque()
        
        for r in range(rows):
            for c in range(cols):
                # fresh oranges
                if grid[r][c]==1:
                    fresh.add((r,c))
                # rotten store in deque
                if grid[r][c]==2:
                    rotten.append((r,c))
                 
        time=0
        while fresh and rotten:
            # print(fresh,rotten)
            for _ in range(len(rotten)):
                r,c=rotten.popleft()
                # check for adjucent oranges
                for adj in ((r,c+1),(r,c-1),(r+1,c),(r-1,c)):
                    if adj in fresh:
                        fresh.remove(adj)
                        rotten.append(adj)
            time+=1
        return -1 if fresh else time