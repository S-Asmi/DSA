class Solution(object):
    def maxSubArray(self, nums):
        maxsub=nums[0]
        sum=0
        for n in nums:
            if sum<0:
                sum=0
            sum=sum+n
            maxsub=max(maxsub,sum)
        return maxsub


        