class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        sum=0
        for i in range(len(startTime)):
            if(queryTime>=startTime[i] and queryTime<=endTime[i]):
                sum=sum+1
        return sum
        