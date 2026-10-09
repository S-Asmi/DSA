class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        ans = []
        cycle = 2 * numRows - 2
        for r in range(numRows):
            for j in range(r, len(s), cycle):
                ans.append(s[j])
                diag_idx = j + cycle - 2 * r
                if 0 < r < numRows - 1 and diag_idx < len(s):
                    ans.append(s[diag_idx])
                    
        return ''.join(ans)

