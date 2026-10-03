class Solution(object):
    def rearrangeArray(self, nums):
        ans=[]
        while nums!=[]:
            renum = sorted(set(nums))
            for i in renum:
                if i in nums:
                    nums.remove(i)
            for i in renum:
                ans.append(i)
        return ans
        