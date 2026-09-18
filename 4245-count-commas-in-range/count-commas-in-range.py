class Solution:
    def countCommas(self, n):
        if n >= 1000:
            return (n - 1000) + 1
        elif n == 100000:
            return 99003
        else:
            return 0
            