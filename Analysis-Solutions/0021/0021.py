# 0021. Merge Two Sorted Lists

#============================================
# Solution#1 Recursion
#============================================
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # base cases
        if l1 == None:
          return l2
          
        if l2 == None:
          return l1
        
        # inductive cases
        if l1.val < l2.val:
          r = self.mergeTwoLists(l1.next,l2)
          l1.next = r
          return l1
        else:
          r = self.mergeTwoLists(l1,l2.next)
          l2.next = r
          return l2
