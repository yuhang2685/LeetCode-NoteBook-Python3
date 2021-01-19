# 0746. Min Cost Climbing Stairs
#
# Note although it is implemented in Recursion style,
# it is still a "Dynamic Programming",
# because it computes the local "optimization" for the global "optimization".
#
# Note it can also be implemented in the non-Recursion style.
# See the standard solution.
#
#====================================
# Solution#1 Dynamic Programming
#====================================
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
        return min(minCostFromLastStep, minCostFromLastLastStep) 
        
