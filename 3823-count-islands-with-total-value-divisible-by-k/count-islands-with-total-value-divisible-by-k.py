from collections import deque

class Solution:
    def countIslands(self, grid, k):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                   
                    queue = deque([(i, j)])
                    visited[i][j] = True
                    total = 0
                    
                    while queue:
                        r, c = queue.popleft()
                        total += grid[r][c]
                        
                        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n:
                                if grid[nr][nc] > 0 and not visited[nr][nc]:
                                    visited[nr][nc] = True
                                    queue.append((nr, nc))
                    
                    if total % k == 0:
                        count += 1
        
        return count