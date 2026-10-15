class Solution(object):
    def sumCounts(self, nums):
        s=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                temp=nums[i:j+1]
                s+=len(set(temp))**2
        return s