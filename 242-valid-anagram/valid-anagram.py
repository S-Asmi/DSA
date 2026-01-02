class Solution(object):
    def isAnagram(self, s,t):
        if(len(s)==len(t)):
            s1=[]
            for i in s:
                s1.append(i)
            for i in t:
                if i in s1:
                    s1.remove(i)
            if(s1==[]):
                return True
            else:
                return False
        else:
            return False
        
        

            


