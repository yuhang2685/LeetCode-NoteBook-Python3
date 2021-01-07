# Wrong Answer
# Input [1,1,1,2,2,3]
# My output [1,2,2,3]
# Note Python use Not instead of ! as "negation", but "!=" is allowed.  

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 1:
            return 0
        
        i = 0
        j = 1
        # Wrong: Should be new = True
        new = False
        
        while j < len(nums):
        
          # Same:
          if nums[i] == nums[j]:
            # See at second time
            if new == True:
              i+=1
              nums[i] = nums[j]
              j+=1
              new = False
            # See at more than second time
            else:
              j+=1
              
          # Diff:    
          else:
            i+=1
            nums[i] = nums[j]
            j+=1
            new = True
                    
        return i+1
       
  
