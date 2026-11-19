from operator import add

MAX_N = 201
DIVS = [[] for _ in range(MAX_N)]
for _d in range(1, MAX_N):
    for _l in range(_d * 2, MAX_N, _d):
        DIVS[_l].append(_d)


class Solution:
    def minimumChanges(self, s, k):
        n = len(s)
        b = s.encode()

        if k == 1:
            best = n
            for d in DIVS[n]:
                changes = 0
                for rem in range(d):
                    l, r = rem, n - d + rem
                    while l < r:
                        if b[l] != b[r]:
                            changes += 1
                        l += d
                        r -= d
                if changes < best:
                    best = changes
                    if not best:
                        return 0
            return best

        INF = 10**9
        max_len = n - 2 * (k - 1)
        cost_T = [[INF] * n for _ in range(n + 1)]

        for d in range(1, max_len // 2 + 1):
            base2 = d * 2
            for i in range(n - base2 + 1):
                j = i + base2
                c = 0
                for rem in range(d):
                    if b[i + rem] != b[i + d + rem]:
                        c += 1
                if c < cost_T[j][i]:
                    cost_T[j][i] = c

                li, rj = i - d, j + d
                while li >= 0 and rj <= n and rj - li <= max_len:
                    for rem in range(d):
                        if b[li + rem] != b[rj - d + rem]:
                            c += 1
                    if c < cost_T[rj][li]:
                        cost_T[rj][li] = c
                    li -= d
                    rj += d

            base3 = d * 3
            if base3 <= max_len:
                for i in range(n - base3 + 1):
                    j = i + base3
                    c = 0
                    for rem in range(d):
                        if b[i + rem] != b[i + base2 + rem]:
                            c += 1
                    if c < cost_T[j][i]:
                        cost_T[j][i] = c

                    li, rj = i - d, j + d
                    while li >= 0 and rj <= n and rj - li <= max_len:
                        for rem in range(d):
                            if b[li + rem] != b[rj - d + rem]:
                                c += 1
                        if c < cost_T[rj][li]:
                            cost_T[rj][li] = c
                        li -= d
                        rj += d

        dp = list(range(1)) + [INF] * n

        for part in range(1, k + 1):
            new_dp = [INF] * (n + 1)
            min_end = part * 2
            max_end = n - (k - part) * 2
            prev_min = (part - 1) * 2
            for j in range(min_end, max_end + 1):
                start_i = max(prev_min, j - max_len)
                new_dp[j] = min(map(add, dp[start_i:j - 1], cost_T[j][start_i:j - 1]))
            dp = new_dp

        return dp[n]