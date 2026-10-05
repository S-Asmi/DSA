class Solution:
    def scoreOfParentheses(self, s):
        s = s.replace("()", "1")

        res = 0
        ct = 1

        for ch in s:
            if ch == '(':
                ct *= 2
            elif ch == ')':
                ct //= 2
            else:
                res += ct

        return res           
    

        