
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        
        i = 0
        j = 1
        
        while j < len(nums):
          if nums[i] != nums[j]:
            i++
            nums[i] = nums[j]
          else:
            j++
        
        return i+1

# Improvement after checking the standard solution:
# 1. The given array is passed by reference, which means the local modifications to the array will be known by caller.
# 2. No i++ in Python but have i+=1
# 3. Wrong with case of one-element array
# 4. Use for-loop on j instead of while-loop, because 2nd-pointer always increase. Sometimes i increased.
