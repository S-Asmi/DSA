class Solution(object):
    def reverseDegree(self, s):
        c=0
        for i in range(len(s)):
            val = ord(s[i]) - ord('a') + 1
            rev_val = 27 - val
            c += (i + 1) * rev_val
        return c
        