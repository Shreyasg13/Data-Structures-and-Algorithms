#     def exist(self, board: List[List[str]], word: str) -> bool:
#         visited={}
#         rows,cols=len(board),len(board[0])
#         for r in range(rows):
#             for c in range(cols):
#                 if self.WordSearch(board,word,r,c,visited):
#                     return True
#         return False
    
#     def WordSearch(self,board,word,r,c,visited,index=0):
        
#         if index==len(word):
#             return True
        
#         if r < 0 or r == len(board) or c<0 or c == len(board[0]) or board[r][c] != word[index] or visited.get((r,c)) :
#                 return False
            
#         visited[(r,c)]=True
#         res=(self.WordSearch(board,word,r,c+1,visited,index+1) or self.WordSearch(board,word,r,c-1,visited,index+1) or
#              self.WordSearch(board,word,r+1,c,visited,index+1) or self.WordSearch(board,word,r-1,c,visited,index+1) )
#         visited[(r,c)]=False            
            
#         return res
    
    
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(row, column, index):
            if index == len(word): return True
            path.add((row, column))
            for r, c in [(row-1, column), (row, column-1), (row, column+1), (row+1, column)]:
                if r in range(M) and c in range(N) and board[r][c] == word[index] and (r, c) not in path:
                    if dfs(r, c, index+1): return True
            path.remove((row, column))
        
        M, N = len(board), len(board[0])
        path = set()
        for row in range(M):
            for column in range(N):
                if board[row][column] == word[0]:
                    if dfs(row, column, 1): return True
        return False
    