# 1. Found a nice solution from 'Discuss' 
class Solution(object):
  def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(nums) != len(set(nums))
    
# 2. Solution using "Dictionary" which is the implementation of "Hash Table" in Python.
# NOTE it only works in Python3 but does not work in Python.
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    d = {}
    for n in nums:
      if n in d.keys():
        return True
      d[n] = 1
    return False

# 3. Solution using Sort followed by comparing adjacent cell contents.

