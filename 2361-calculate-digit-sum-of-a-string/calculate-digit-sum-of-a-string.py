class Solution:
    def digitSum(self, s, k):
        while len(s) > k:
            while len(s) % k != 0:
                s += '0'

            new_s = ''
            i = 0
            while i < len(s):
                total = 0
                j = i
                while j < i + k:      
                    total += int(s[j])
                    j += 1
                new_s += str(total)
                i += k               
            s = new_s
        return s





        

        