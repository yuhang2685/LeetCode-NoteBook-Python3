# 0002. Add Two Numbers
#
#=================================
# Solution#1 - Straight Forward
#=================================
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      
      l3 = ListNode(0)
      rst = l3
      c = 0
      
      while l1 or l2:
        
        if l1:
          d1 = l1.val
          l1 = l1.next
        else:
          d1 = 0
          
        if l2:
          d2 = l2.val
          l2 = l2.next
        else:
          d2 = 0
          
        d1 = d1 + d2 + c
        
        if d1 > 9:
          d1 -= 10
          c = 1
        else:
          c = 0
                
        l3.next = ListNode(d1)
        l3 = l3.next
      
      if c != 0:      
        l3.next = ListNode(1)
      
      return rst.next
