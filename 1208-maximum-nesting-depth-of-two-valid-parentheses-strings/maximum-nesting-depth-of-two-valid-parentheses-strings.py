class Solution:
    def maxDepthAfterSplit(self, seq):
        res = []

        for i in range(len(seq)):
            res.append((i ^ ord(seq[i])) & 1)

        return res
        