class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        val = [val for val in range(n)]
        if nums == val:
            return 0
        if nums == sorted(val,reverse=True):
            return 1
        li = [False] * n
        rd = [False] * n
        li[0] = True
        rd[n-1] = True
        for i in range(1,n):
            if nums[i] > nums[i-1] and li[i-1]:
                li[i] = True
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1] and rd[i+1]:
                rd[i] = True
        for i in range(n-1):
            if li[i] and rd[i+1] and nums[-1] < nums[0]:
                return min(i+1,n-i+1)
                
        ld = [False] * n
        ri = [False] * n
        ld[0] = True
        ri[n-1] = True
        for i in range(1,n):
            if nums[i] < nums[i-1] and ld[i-1]:
                ld[i] = True
        for i in range(n-2,-1,-1):
            if nums[i] > nums[i+1] and ri[i+1]:
                ri[i] = True
        for i in range(n-1):
            if ld[i] and ri[i+1] and nums[-1] > nums[0]:
                return min(i+1,n-i-1)+1
        return -1