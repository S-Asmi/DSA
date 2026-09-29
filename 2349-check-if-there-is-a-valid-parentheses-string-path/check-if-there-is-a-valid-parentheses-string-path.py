class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2:
            return False
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                cur = set()

                change = 1 if grid[i][j] == '(' else -1

                # Starting cell
                if i == 0 and j == 0:
                    if change >= 0:
                        cur.add(change)
                else:
                    # From above
                    if i > 0:
                        for balance in dp[j]:
                            new_balance = balance + change
                            if new_balance >= 0:
                                cur.add(new_balance)

                    # From left
                    if j > 0:
                        for balance in dp[j - 1]:
                            new_balance = balance + change
                            if new_balance >= 0:
                                cur.add(new_balance)

                dp[j] = cur

        return 0 in dp[n - 1]