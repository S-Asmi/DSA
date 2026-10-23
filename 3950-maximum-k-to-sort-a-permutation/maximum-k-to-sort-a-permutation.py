class Solution:
    def sortPermutation(self, nums):
        res = None

        for i, x in enumerate(nums):
            if x != i:
                res = x if res is None else res & x

        return 0 if res is None else res