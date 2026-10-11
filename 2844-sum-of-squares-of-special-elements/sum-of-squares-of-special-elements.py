class Solution(object):
    def sumOfSquares(self, nums):
        s=0
        for i in range(0,len(nums)):
            if len(nums)%(i+1)==0:
                s=s+(nums[i]*nums[i])
        return s