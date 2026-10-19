class Solution:
    def targetIndices(self, nums, target):
        nums.sort()
        try:
            first = nums.index(target)
        except:
            return []
        last = len(nums) - 1 - nums[::-1].index(target)
        if first == last:
            return [first]
        else:
            return list(range(first, last+1))
        