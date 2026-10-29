import sys

class Solution:
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        LOGN = 16 
        up = [[0] * LOGN for _ in range(n)]
        
        timer = 1
        iters = [iter(adj[u]) for u in range(n)]
        stack = [0]
        tin[0] = timer
        timer += 1
        depth[0] = 0
        
        while stack:
            u = stack[-1]
            try:
                v = next(iters[u])
                if v != up[u][0]:  
                    up[v][0] = u
                    depth[v] = depth[u] + 1
                    tin[v] = timer
                    timer += 1
                    stack.append(v)
            except StopIteration:
                tout[u] = timer - 1
                stack.pop()
        for j in range(1, LOGN):
            for i in range(n):
                up[i][j] = up[up[i][j - 1]][j - 1]
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOGN):
                if (diff >> j) & 1:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOGN - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]
        tree_size = n + 5
        tree = [0] * tree_size
        
        def range_update(l, r, val):
            idx = l
            while idx < tree_size:
                tree[idx] ^= val
                idx += idx & -idx
            idx = r + 1
            while idx < tree_size:
                tree[idx] ^= val
                idx += idx & -idx
                
        def point_query(pos):
            res = 0
            idx = pos
            while idx > 0:
                res ^= tree[idx]
                idx -= idx & -idx
            return res
        cur_mask = [1 << (ord(c) - 97) for c in s]
        for i in range(n):
            range_update(tin[i], tout[i], cur_mask[i])
            
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - 97)
                diff = cur_mask[u] ^ new_mask
                if diff != 0:
                    range_update(tin[u], tout[u], diff)
                    cur_mask[u] = new_mask
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                path_mask = point_query(tin[u]) ^ point_query(tin[v]) ^ cur_mask[lca]
                ans.append((path_mask & (path_mask - 1)) == 0)
                
        return ans
        