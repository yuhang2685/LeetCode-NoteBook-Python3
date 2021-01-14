# 202. Happy Number
#
# Note the question is straight forward, except that to be able to avoid the endless loop you have to stop if you find a already seen number.
#
class Solution:
    def isHappy(self, n: int) -> bool:
      mem = set()
      while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])
        if n in mem:
            return False
        else:
            mem.add(n)
 
      return True
        
