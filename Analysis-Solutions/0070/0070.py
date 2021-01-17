# 0070. Climbing Stairs 
#
# Note:
# 1. We remove case "n == 0" because it is included in the other two base cases.
# 2. "Solution#1 Recusion" got the error of "Time Limit Exceeded".
#    The reason is in this recursion, the inductive case is the combination of two sub-components which share too many redundent sub-components.
#    One way to solve this "heavy redundent issue" is to use an extra memory to store the computed sub-components in "popping".
#    There after our recursion reaches the base cases, we come back with results by using mem instead of a calculation. (Not quite right, see later errors)
# 3. "Solution#1 Recusion with memory" got the error "list index out of range" in "return self.helper(n, mem[n])".
# 4. "Solution#1 Recusion with global memory" still got "Time Limit Exceeded".
#    The reason is we did not understand the solving for "heavy redundent issue".
#    The "real" reducing does not happen in the first branch recursion, which is still a standard recursion style "push-pop".
#    The reducing happens in the second or later recursion when the result was already computed and stored in mem
#    by the earlier branch recursion, and so does not need to recursion this time.
#    See "Solution#1 Recusion with global memory - Correct".
#=================================
# Solution#1 Recusion - Incorrect
#=================================
class Solution:
    def climbStairs(self, n: int) -> int:        
        # base cases
        if n == 0:
          return 1
        
        if n == 1:
          return 1
        
        if n == 2:
          return 2
        
        # inductive cases
        return 1 * self.climbStairs(n - 1) + 1 * self.climbStairs(n - 2)
#====================================
# Solution#1 Recusion with memory - Incorrect
#====================================
class Solution:
    
    def climbStairs(self, n: int) -> int:
        mem = []
        return self.helper(n, mem[n])
        
    def helper(self, n, mem):    
    
        # base cases
        if n == 1:
          mem[1] = 1
          return mem[1] 
        
        if n == 2:
          mem[2] = 1
          return mem[2]
        
        # inductive cases
        mem[n] = self.helper(n-1, mem) + self.helper(n-2, mem)
        return mem[n]
        
#======================================================
# Solution#1 Recusion with global memory - Correct
#======================================================                
class Solution:
    def __init__(self):
        
        self.mem = {}
    
    def climbStairs(self, n: int) -> int:    
        
        if n in self.mem:
            return self.mem[n]
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        else:
            result = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.mem[n] = result
            return result
