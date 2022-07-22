class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        Matrix=[[1 for i in range(n) ]for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                Matrix[i][j] = Matrix[i-1][j] + Matrix[i][j-1]
            print(Matrix)
        return Matrix[-1][-1]
