class Solution(object):
    def climbStairs(self, n, costs):
        if n==1:
            return costs[0]+1
        res=[0]*(n+1)
        res[1]=costs[0]+1
        res[2]=costs[1]+min(4,res[1]+1)
        for i in range(3,n+1):
            res[i]=min(res[i-3]+costs[i-1]+9,res[i-2]+costs[i-1]+4,res[i-1]+costs[i-1]+1)
        return res[-1]