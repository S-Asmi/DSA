class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        sum=0
        for i in range(len(timeSeries)-1):
            j=min(duration,timeSeries[i+1]-timeSeries[i])
            sum=sum+j
        sum=sum+duration
        return sum 

        