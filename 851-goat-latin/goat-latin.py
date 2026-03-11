class Solution(object):
    def toGoatLatin(self, sentence):
        og=sentence.split()
        new=[]
        j=1
        for i in og:
            if i[0]=='a'or i[0]=='e'or i[0]=='i'or i[0]=='o'or i[0]=='u'or i[0]=='A'or i[0]=='E'or i[0]=='I'or i[0]=='O'or i[0]=='U':
                new.append(i+'ma'+'a'*(j))
                j=j+1
            else:
                new.append(i[1:]+i[0]+'ma'+'a'*(j))
                j=j+1
        res=' '.join(new)
        return res

        