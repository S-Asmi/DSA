class Solution:
    def countCommas(self, n):
        count, p = 0, 1000

        while p <= n:
            count += n - p + 1
            p *= 1000

        return count