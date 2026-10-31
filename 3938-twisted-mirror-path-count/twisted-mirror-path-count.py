class Solution(object):
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        def resolve(i, j, direction):
            seen = set()
            while 0 <= i < m and 0 <= j < n:
                state = (i, j, direction)
                if state in seen:
                    return None
                seen.add(state)
                if grid[i][j] == 0:
                    return (i, j)
                if direction == 0: 
                    i += 1
                    direction = 1
                else:  
                    j += 1
                    direction = 0
            return None
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or dp[i][j] == 0:
                    continue
                if j + 1 < n:
                    land = resolve(i, j + 1, 0)
                    if land:
                        x, y = land
                        dp[x][y] = (dp[x][y] + dp[i][j]) % MOD
                if i + 1 < m:
                    land = resolve(i + 1, j, 1)
                    if land:
                        x, y = land
                        dp[x][y] = (dp[x][y] + dp[i][j]) % MOD
        
        return dp[m - 1][n - 1]