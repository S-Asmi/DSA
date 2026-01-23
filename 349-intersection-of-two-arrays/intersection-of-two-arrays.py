class Solution(object):
    def intersection(self, nums1, nums2):
        result=[]
        for i in nums1:
            if i in nums2:
                result.append(i)
        r=list(set(result))
        return r
    
        