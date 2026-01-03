class Solution(object):
    def rob(self, nums):
        sum1=0
        sum2=0
        for i in nums:
            temp=max(i+sum1,sum2)
            sum1=sum2
            sum2=temp
        return sum2
        
    
        