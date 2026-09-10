class Solution:
    def getMinDistance(self, nums, target, start):
        mindist = float('inf')
        for i, num in enumerate(nums):
            if num == target:
                mindist = min(mindist, abs(i - start))
        return mindist