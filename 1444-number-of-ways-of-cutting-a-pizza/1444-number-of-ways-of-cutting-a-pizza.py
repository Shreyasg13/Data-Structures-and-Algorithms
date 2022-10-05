class Solution:
    def ways(self, grid, k):
        dp = {}
        def count(a, b, c, d):
            return total[c][d] - total[a][d] - total[c][b] + total[a][b]
            
        def dfs(a, b, k):
            if (a, b, k) in dp: return dp[(a, b, k)]
            if k == 1 and count(a, b, row, col) >= 1: return 1

            ret, mod = 0, int(1e9 + 7)
            for i in range(a + 1, row):
                if count(a, b, i, col) >= 1:
                    ret = (ret + dfs(i, b, k - 1)) % mod
            for j in range(b + 1, col):
                if count(a, b, row, j) >= 1:
                    ret = (ret + dfs(a, j, k - 1)) % mod
            dp[(a, b, k)] = ret
            return ret
            
        row, col = len(grid), len(grid[0])
        x, y = row + 1, col + 1
        total = [[0] * y for _ in range(x)]
        for i in range(1, x):
            for j in range(1, y):
                total[i][j] = total[i-1][j] + total[i][j-1]- total[i-1][j-1] + int(grid[i-1][j-1] == 'A')

        
        
        return dfs(0, 0, k)