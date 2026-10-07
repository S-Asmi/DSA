class Solution(object):
    def removeInvalidParentheses(self, s):
        res, removed, count = {s}, 0, {'(':0, ')':0}
        for i, c in enumerate(s):
            if c == ')' and count['('] == count[')']:
                resupdate = set()
                while res:
                    substr = res.pop()
                    for j in range(i-removed+1):
                        if substr[j] == ')':  
                            resupdate.add(substr[:j]+substr[j+1:])
                res = resupdate
                removed += 1
            else:
                if c in count: count[c] += 1
        n, count = len(s), {'(':0, ')':0}
        for i in range(n-removed-1, -1, -1):
            n -= 1; c = s[n]
            if c == '(' and count['('] == count[')']:
                resupdate = set()
                while res:
                    substr = res.pop()
                    for j in range(i, len(s)-removed):
                        if substr[j] == '(':   
                            resupdate.add(substr[:j]+substr[j+1:])
                res = resupdate
                removed += 1
            else:
                if c in count: count[c] += 1
        return list(res)