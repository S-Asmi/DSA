class Solution(object):
    def searchMatrix(self, matrix, target):
        mx, nx = len(matrix), len(matrix[0])
        m, n = 0, nx - 1 

        while m< mx and n >= 0:
            current = matrix[m][n]
            if current == target:
                return True 
            elif target < current:
                n -= 1 
            else:
                m += 1  
        return False  
        