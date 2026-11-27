class Solution(object):
    def maximumSaleItems(self, items, budget):
        
    
        n = len(items)
        bonus = [0] * n

        for i in range(n):
            fi = items[i][0]
            cnt = 0

            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    cnt += 1

            bonus[i] = cnt

        NEG = -10**18

        dp = [NEG] * (budget + 1)
        dp[0] = 0
        for idx in range(n):
            p = items[idx][1]   # price
            b = bonus[idx]

            ndp = dp[:]

            for r in range(p):
                best = NEG

                m = 0
                c = r

                while c <= budget:
                    if m >= 1:
                        best = max(best, dp[c - p] - (m - 1))

                    if best != NEG:
                        ndp[c] = max(ndp[c], best + m + b)

                    m += 1
                    c += p

            dp = ndp

        return max(dp)