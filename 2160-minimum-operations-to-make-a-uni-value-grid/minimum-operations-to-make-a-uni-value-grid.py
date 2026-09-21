class Solution:
    def minOperations(self, grid, x):
        arr = [num for row in grid for num in row]
        arr.sort()
        median = arr[len(arr) // 2] 
        for num in arr:
            if (num - median) % x != 0:
                return -1 
        return sum(abs(num - median) // x for num in arr)