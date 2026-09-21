class Solution:
    def minOperations(self, grid, x):
        arr = [num for row in grid for num in row]
        arr.sort()
        mid = arr[len(arr) // 2] 
        for num in arr:
            if (num - mid) % x != 0:
                return -1 
        return sum(abs(num - mid) // x for num in arr)