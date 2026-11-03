class Solution:
    def minMoves(self, nums):
        mv = max(nums)
        count = 0
        for i in nums:
            count += (mv - i)
        
        return count