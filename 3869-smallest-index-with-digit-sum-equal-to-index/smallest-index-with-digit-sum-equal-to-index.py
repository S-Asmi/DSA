class Solution(object):
    def smallestIndex(self, nums):
        for i in range(0,len(nums)):
            sum=0
            x=nums[i]
            while x>0:
                sum+=x%10
                x//=10
            if sum==i:
                return i
            
        return -1
        