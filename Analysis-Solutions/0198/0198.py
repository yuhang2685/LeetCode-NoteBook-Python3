# 0198. House Robber
#
# Note:
# The problem is very similar to 0746.
#
#========================================================
# Solution#1 Dynamic Programming
#========================================================
class Solution:
    
    def __init__(self):
        self.mem = {}
    
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) in self.mem:
            return self.mem[len(nums)]
        
        # base cases
        if len(nums) == 0:         
          return 0
        
        if len(nums) == 1:
          self.mem[1] = nums[0]
          return self.mem[1]
        
        if len(nums) == 2:
          self.mem[2] = max(nums[0], nums[1])
          return self.mem[2]
        
        # inductive cases        
        climbedFromLastStep     = self.rob(nums[:-1])
        climbedFromLastLastStep = self.rob(nums[:-2]) + nums[len(nums)-1]
        self.mem[len(nums)] = max(climbedFromLastStep, climbedFromLastLastStep)
        
        return self.mem[len(nums)]
        
