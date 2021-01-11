# 0234. Palindrome Linked List
#
# Note
# We first try the inductive cases by holding "head" 
# and throwing the rest (called "tail" in recursion?) into the function
# and pretend it returns correct result.
# However, the rests always contain elements more than needed, say the end of the LinkedList.
# 
# Then we check with otherone's solution, it is tricky.
# We decide to leave it now and come back in future.
#
#==================================
# Solution#1 Recursion (Incorrect, come back later)
#==================================
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # base cases
        if head == None:
          return True
          
        if head.next == None:
          return True        
        
        # inductive cases
        
        r = self.isPalindrome(head.next)
        
