# 0344. Reverse String
#
# Notes:
#
# We only supply the solutions for Recursion. 
# Solution#1 violates restriction "O(1) space", it still worth for practicing.
#
# Solution#2 does not work, I guess because the function is fixed to in-place working on the input string.
# Therefore solution#2 works on generating a new string which is different to the input string.
# But the algorithm is good for inspiration.
#
# Other solutions are straight forward.


#==========================================
# Solution#1: Recursion with helper
#==========================================
class Solution:
        
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.helper(s, 0, len(s)-1)
        return
        
    def helper(self, s: List[str], left: int, right: int) -> None:
    
        # base cases
        if left >= right:
            return
        
        # inductive cases
        else:
            temp = s[right]
            s[right] = s[left]
            s[left] = temp
            self.helper(s, left+1, right-1)
            return
            
#=============================================
# Solution#2: Recursion - Only for inspiration
#=============================================
class Solution:
        
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """        
      
        l = len(s)
        if length <= 1:
            return s
        else:
            return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])
            
            

