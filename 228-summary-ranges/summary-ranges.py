class Solution(object):
    def summaryRanges(self, nums):
        result = []
        if not nums:
            return result
        start = nums[0]
        end = nums[0]
        for n in nums[1:]:
            if n == end + 1:
                end = n
            else:
                if start == end:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(end))
                start = n
                end = n
        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(end))
        return result