# 0203. Remove Linked List Elements
#
# NOTE
#
# Solution#1 straight forward "Prev-Curr Runner".
#
# Then we optimized by merging the work of "Curr" to "Prev", because "Curr" is always the next to "Prev".
# Note the merge is not applicable to problems using "Two Pointers" in Arrays, since we do not want to shift the rest of array at each step.
#
# Solution#2 Recursion.

#========================================
# Solution#1: Prev-Curr Runner
#========================================
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
  
      # Initialization
      dummy = ListNode(0)
      dummy.next = head    
      prev = dummy
      curr = head
      
      # Travel through the LinkedList
      while curr:
        
        # Found val
        if curr.val == val:
          prev.next = curr.next
        else:
          prev = prev.next
          
        curr = curr.next
            
      # Done the work
      return dummy.next 
      
#========================================
# Solution#1: Single pointer
#========================================
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

      # Initialization
      dummy = ListNode(0)
      dummy.next = head    
      prev = dummy
      
      # Travel through the LinkedList
      while prev and prev.next:
        
        # Found val
        if prev.next.val == val:
          prev.next = prev.next.next
        prev = prev.next          
            
      # Done the work
      return dummy.next 
      
#========================================
# Solution#2: Recursion
# Note it can be more concise, but current version is easy to understand
#========================================
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

      # Base cases
      if head == None:
        return head
      
      # Inductive cases
      if head.val == val:
        head = head.next
        return self.removeElements(head, val)  
        
      if head.val != val:
        head.next = self.removeElements(head.next, val)  
        return head     
      
      
      
      
