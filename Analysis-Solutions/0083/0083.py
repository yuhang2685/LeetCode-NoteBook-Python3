# 0083. Remove Duplicates from Sorted List
#
# Note: The tricky part is in the inductive case, we have to do comparision after the sub list is returned.
#       Otherwise it fails for the case "head == head.next.next", i.e., [1,1,1,1,1,1,1].
#
#=========================================
# Solution#1 Recursion
#=========================================
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
      
      # base cases
      if head == None:
        return head
        
      if head.next == None:
        return head      
      
      # inductive cases
      #----------------------------------------------------
      #if head.val == head.next.val:
      #  head.next = self.deleteDuplicates(head.next.next)
      #  return head
      #else:
      #  head.next = self.deleteDuplicates(head.next)
      #  return head
      #----------------------------------------------------
      # r has no duplicates
      r = self.deleteDuplicates(head.next)
      if head.val == r.val:
        head.next = r.next
        return head
      else:
        head.next = r
        return head
