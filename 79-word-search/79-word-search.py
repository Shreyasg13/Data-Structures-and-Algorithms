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
    
    
def dfs(board, word, r, c, visited):
    if not word:
        return True

    if (
        (r, c) in visited
        or r < 0
        or r >= len(board)
        or c < 0
        or c >= len(board[0])
        or board[r][c] != word[0]
    ):
        return False

    return (
        dfs(board, word[1:], r + 1, c, visited + [(r, c)])
        or dfs(board, word[1:], r - 1, c, visited + [(r, c)])
        or dfs(board, word[1:], r, c + 1, visited + [(r, c)])
        or dfs(board, word[1:], r, c - 1, visited + [(r, c)])
    )


class Solution:
    def exist(self, board, word):
        for r, row in enumerate(board):
            for c, l in enumerate(row):
                if dfs(board, word, r, c, []):
                    return True
        return False