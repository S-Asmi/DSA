class Solution:
    def nextGreaterElement(self, nums1, nums2):
        next_greater = {}
        stack = []

        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            next_greater[num] = -1 if not stack else stack[-1]
            stack.append(num)

        return [next_greater[num] for num in nums1]