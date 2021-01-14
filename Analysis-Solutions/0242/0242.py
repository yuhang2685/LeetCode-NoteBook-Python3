#======================================
# Solution#1 Sorting
#======================================
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
#======================================
# Solution#2 Hash Table
#======================================
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s, d_t = {}, {}
        for c in s:
          d_s[c] = d_s.get[c,0] + 1
        for c in t:
          d_t[c] = d_t.get[c,0] + 1
        return d_s == d_t 
        
#======================================
# Solution#3 Size-26 Array
#======================================
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      a_s, a_t = [0]*26, [0]*26
      for c in s:
        a_s[ord(c) - ord('a')] += 1
      for c in t:
        a_t[ord(c) - ord('a')] += 1
      return a_s == a_t  
