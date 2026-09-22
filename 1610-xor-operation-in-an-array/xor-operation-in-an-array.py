class Solution:
    def xorOperation(self, n, start):
        ans = 0

        while n:
            ans ^= start
            start += 2
            n -= 1

        return ans
        