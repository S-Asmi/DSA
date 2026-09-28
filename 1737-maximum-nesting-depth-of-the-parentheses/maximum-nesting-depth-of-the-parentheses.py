class Solution:
    def maxDepth(self, s):
        op = 0
        stk = []

        for i in s:
            if i == '(':
                stk.append(i)

            elif i == ')':
                stk.pop()

            op = max(op, len(stk))

        return op