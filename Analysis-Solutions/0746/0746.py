# 0746. Min Cost Climbing Stairs
#
# Note although it is implemented in Recursion style,
# it is still a "Dynamic Programming",
# because it computes the "local optimization" for the "global optimization".
#
# Note it can also be implemented in the "non-Recursion" style which is often called "iteration",
# which has the advantege of O(1) space instead of O(n) for Recursion stack.
# See the standard solution.
#
# "Solution#1 Dynamic Programming - Time Limit Exceeded" due to the redundant computation in recursion.
#
# Note in "Solution#1 Dynamic Programming - Dictionary memory" 
# we use Dictionary instead of Array/List (Python has List instead of Array)
# because we do not want to care about Array initialization 
# with size of array which is not an argument for "__init__()",
# and the operations of Dictionary share many same syntax with Array,
# which is confusing.
#
# We also tried defining "dp" as a global array, but failed due to being unskilled in Python.
#
#========================================================
# Solution#1 Dynamic Programming - Time Limit Exceeded
#========================================================
class Solution(object):
    def minCostClimbingStairs(self, cost):
        
        # base cases
        if len(cost) == 1:
          return 0
                 
        if len(cost) == 0:
          return 0
        
        # inductive cases
        minCost_climbedFromLastStep     = cost[-1]+self.minCostClimbingStairs(cost[:-1])
        minCost_climbedFromLastLastStep = cost[-2]+self.minCostClimbingStairs(cost[:-2])
        return min(minCost_climbedFromLastStep, minCost_climbedFromLastLastStep) 

    
#=======================================================
# Solution#1 Dynamic Programming - Dictionary memory
#=======================================================
class Solution(object):
    
    def __init__(self):
        self.dp = {}
        
    def minCostClimbingStairs(self, cost):                
        
        if len(cost) in self.dp:
          return self.dp[len(cost)]
        
        # base cases
        if len(cost) == 1:
          return 0
                 
        if len(cost) == 0:
          return 0
        
        # inductive cases
        minCost_climbedFromLastStep     = cost[-1]+self.minCostClimbingStairs(cost[:-1])
        minCost_climbedFromLastLastStep = cost[-2]+self.minCostClimbingStairs(cost[:-2])
        self.dp[len(cost)] = min(minCost_climbedFromLastStep, minCost_climbedFromLastLastStep) 
        return self.dp[len(cost)]
    
    
    
