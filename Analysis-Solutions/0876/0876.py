# NOTES:
#
# It restricts to output the second middle node if there are two middle nodes.
#
# Our primitive try works fine for a unique middle node, but outputs the first middle node if there are two middle nodes.
# Therefore we first experiment to initialize ptr2 to the next of the head (one step ahead) to see what happens.
# Such initialization is allowed because the given LinkedList is non-empty.
# But it doesn't work. Comparing with the primitive try, it stops at the last to the end where pt1 is still at the first middle node.
#
# Noticed that, intuitively we think about distinguish the case of odd and even length, e.g., ptr1 moves one more step if length is even.
# It sounds a little bit clumsy because it brings too much extra works.
# Then inspired by the first experiment where ptr2 stops at the last to the end instead of the end,
# we come up with an idea: why not stop ptr2 a step futher, say ptr2 stops at the next to the end in that case?
# Therefore instead of primitive one ptr2 stops at either the end or the last to the end,
# we will let ptr2 stop at either the end or the next to the end which is a "None" node.
# We change the loop condition and the loop body to make it.


#=========================================================
# Solution#1 Slow-Fast Runner
#=========================================================
# Primitive try doesn't work
#---------------------------------------------------------
class Solution:
  def middleNode(self, head: ListNode) -> ListNode:
    
    # Initialization
    ptr1 = head
    ptr2 = head
    
    # Travel until ptr2 reaches the end
    while ptr2 != None and ptr2.next != None:    
      ptr1 = ptr1.next
      ptr2 = ptr2.next.next
    
    # ptr2 reaches the end
    return ptr1
#-------------------------------------------------
# Modified solution does work
#-------------------------------------------------
class Solution:
  def middleNode(self, head: ListNode) -> ListNode:
    
    # Initialization
    ptr1 = head
    ptr2 = head
    
    # Travel until ptr2 reaches the end
    #while ptr2 != None and ptr2.next != None:        
    while ptr2 != None:        
      if ptr2.next == None:  
        return ptr1
      ptr1 = ptr1.next
      ptr2 = ptr2.next.next
    
    # ptr2 reaches the end
    return ptr1
    
#==========================================
# Solution#2 Count length and travel again
#==========================================
class Solution(object):
    def middleNode(self, head):
        
        count = 0
        p = head
        
        while p:
          count += 1
          p = p.next
        
        mid = count // 2
        p = head
        
        while mid > 0:
            p = p.next
            mid -= 1
        
        return p

#==========================================
# Solution#3 Hash Table
#==========================================
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        dict = {}        
        i = 0
        
        while head:                     
          dict[i] = head
          head = head.next
          # Note when the loop ends, i points to "None".
          i += 1         
          
        mid = i // 2        
        return dict[mid]
        
