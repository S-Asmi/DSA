class Solution:
    def closedIsland(self, grid):
        
        def dfs(i, j):
            grid[i][j] = 1
            adj = [ [i-1, j], [i+1, j], [i, j-1], [i, j+1] ]
            
            for a, b in adj:
                if a<0 or a==m or b<0 or b==n or grid[a][b] == 1:
                    continue
                dfs(a, b)
            
        m, n = len(grid), len(grid[0])

        for j in range(n):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[m-1][j] == 0:
                dfs(m-1, j)
            
        for i in range(1, m-1):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][n-1] == 0:
                dfs(i, n-1)
        
        count = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 0:
                    count += 1
                    dfs(i, j)
        return count