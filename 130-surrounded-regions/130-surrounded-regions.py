class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # visited=set()
        rows,cols=len(board),len(board[0])
        def DFS(r,c):
            
            if (r < 0 or r > rows-1 or c <0  or c > cols-1 or
                board[r][c]!="O"):
                return 
            
            board[r][c]="Z"
            DFS(r,c+1)
            DFS(r,c-1)
            DFS(r+1,c)
            DFS(r-1,c)
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and (r in [0,rows-1] or c in [0,cols-1]):
                    DFS(r,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="Z":
                    board[r][c]="O"
        