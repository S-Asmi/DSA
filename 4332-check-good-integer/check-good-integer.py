class Solution:
    def checkGoodInteger(self, n):
        value = str(n)
        square_sum, digit_sum = 0, 0
        for i in range(len(value)):
            digit_sum += int(value[i])
            square_sum += int(value[i]) ** 2
        return True if square_sum - digit_sum >= 50 else False

        