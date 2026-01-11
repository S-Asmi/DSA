class Solution(object):
    def containsDuplicate(self, nums):
        dup=set(nums) 
        if len(dup)==len(nums):
            return False
        else:
            return True