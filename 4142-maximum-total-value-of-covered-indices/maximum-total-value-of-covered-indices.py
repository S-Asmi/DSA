class Solution(object):
    def solve(self,nums,s,i,prev,cache):
        if i == len(nums):
            return 0

        if (i,prev) in cache:
            return cache[(i,prev)]    
        ans = 0
        if s[i] == "1":
          
           if i > 0:
             a = 0
             if prev == 0:
               a = nums[i-1] + self.solve(nums,s,i+1,0,cache)
             b = nums[i] + self.solve(nums,s,i+1,1,cache)
             ans = max(a,b)
           else:
             ans = nums[i] + self.solve(nums,s,i+1,1,cache)
                      
        else:
            ans = self.solve(nums,s,i+1,0,cache)
        
        cache[(i,prev)] = ans
        return ans    


    def maxTotal(self, nums, s):
        """
        :type nums: List[int]
        :type s: str
        :rtype: int
        """
        s = list(s)
        return self.solve(nums,s,0,0,{})
        