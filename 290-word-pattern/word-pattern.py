class Solution(object):
    def wordPattern(self, pattern, s):
        a = {}
        t = s.split()
        if len(pattern) != len(t):
            return False
        j = 0
        for i in pattern:
            if i not in a:
                if t[j] in a.values():
                    return False
                a[i] = t[j]
            else:
                if a[i] != t[j]:
                    return False
            j = j + 1
            
        return True
                
            
        