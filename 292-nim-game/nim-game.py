class Solution(object):
    def canWinNim(self, n):
        if n<=3:
            return True
        
        else:
            return n % 4 != 0
        
        