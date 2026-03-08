class Solution:
    def canJump(self, nums):
        j = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= j:
                j = i
        return j == 0