class Solution(object):
    def maxAlternatingSum(self, nums):
        m=0
        l=[]
        for x in nums:
            l.append(x**2)
        l.sort()
        i=0
        while i<len(l)//2:
            m+=l[-1-i]-l[i]
            i+=1
        return m if len(l)%2==0 else m+l[len(l)//2]