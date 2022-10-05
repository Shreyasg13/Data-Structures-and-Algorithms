class Solution:
    def ways(self, grid, k):
        n, m = len(grid), len(grid[0])
        N, M = n + 1, m + 1
        sum_grid = [[0] * M for _ in range(N)]
        for i in range(1, N):
            for j in range(1, M):
                sum_grid[i][j] = sum_grid[i-1][j] + sum_grid[i][j-1]\
                               - sum_grid[i-1][j-1] + int(grid[i-1][j-1] == 'A')

        dp = {}
        def count(a, b, c, d):
            return sum_grid[c][d] - sum_grid[a][d]\
                 - sum_grid[c][b] + sum_grid[a][b]
        def dfs(a, b, k):
            if (a, b, k) in dp: return dp[(a, b, k)]
            if k == 1 and count(a, b, n, m) >= 1: return 1

            ret, mod = 0, int(1e9 + 7)
            for i in range(a + 1, n):
                if count(a, b, i, m) >= 1:
                    ret = (ret + dfs(i, b, k - 1)) % mod
            for j in range(b + 1, m):
                if count(a, b, n, j) >= 1:
                    ret = (ret + dfs(a, j, k - 1)) % mod
            dp[(a, b, k)] = ret
            return ret

        return dfs(0, 0, k)