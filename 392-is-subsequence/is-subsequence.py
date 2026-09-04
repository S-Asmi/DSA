class Solution:
    def isSubsequence(self, s, t):
        n1 = len(s)
        n2 = len(t)

        if n1 == 0:
            return True
        if n1 > n2:
            return False

        idx = 0

        for i in range(n2):
            if t[i] == s[idx]:
                idx += 1
            if idx == n1:
                return True

        return idx == n1