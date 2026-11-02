import random

class Solution:
    def minMoves2(self, nums):
        k=len(nums)//2

        def quickselect(left, right):
            pivot=nums[random.randint(left, right)]
            i,j=left, right

            while i<=j:
                while nums[i]<pivot:
                    i += 1
                while nums[j]>pivot:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1

            if k <= j:
                return quickselect(left,j)
            if k >= i:
                return quickselect(i,right)
            return nums[k]

        median = quickselect(0, len(nums) - 1)
        return sum(abs(x - median) for x in nums)