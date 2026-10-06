class Solution(object):
    def reverseWords(self, s):
        m=s.split()
        res=""
        n=len(m)
        for i in range(-1, -(n+1),-1):
            res=res+m[i]+' '
        return res.rstrip()

        
        