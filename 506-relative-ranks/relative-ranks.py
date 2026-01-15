class Solution(object):
    def findRelativeRanks(self, score):
        x = sorted(score)[::-1]
        a = []
        for i in score:
            if x.index(i)==0:
                a.append("Gold Medal")
            elif x.index(i)==1:
                a.append("Silver Medal")
            elif x.index(i)==2:
                a.append("Bronze Medal")
            else:
                a.append(str(x.index(i)+1))
        return a   