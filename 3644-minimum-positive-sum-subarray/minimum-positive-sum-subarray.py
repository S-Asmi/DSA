class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        n=len(nums)
        pre=[0]*(n+1)
        for idx in range(n):
            pre[idx+1]=nums[idx]+pre[idx]
        res=float("inf")
        for length in range(l,r+1):
            for idx in range(length,n+1):
                if pre[idx]-pre[idx-length]>0:
                    res=min(res,pre[idx]-pre[idx-length])
        return -1 if res==float("inf") else res