#1. Solution#1 we need to add another guard "head != None" for empty LinkedList
#2. Solution#1 "#while ptr2.next != None and ptr2.next.next != None:" is overkilled, should be "while ptr2 != None and ptr2.next != None:".
#3. Solution#2 is inefficient in Python3.
#4. Solution#2 "if d[ptr] == 1:" causes error, should be replaced by "if ptr in d:".
#5. Solution#3 noticed *Dictionary* is used to track node and we don't care about value, so we furthermore replace *Dictionary* by "Set". 
#========================================================================
# Solution#1: Slow-Fast Runner
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def hasCycle(self, head: ListNode) -> bool:
    
    # Guard
    #if head.next == None:
    #if head == None or head.next == None:
    if head == None:
     return False
    
    # Initialization
    ptr1=head
    ptr2=head.next
    
    # Travelling along the LinkedList to the end
    #while ptr2.next != None and ptr2.next.next != None:
    while ptr2 != None and ptr2.next != None:
    
      # Found cycle
      if ptr1 == ptr2:
        return True
      
      # Found no cycle, move on
      ptr1 = ptr1.next 
      ptr2 = ptr2.next.next
    
    # ptr2 reaches the end, found no cycle
    return False;  

#==========================================================
# Solution#2: Hash Table
class Solution:
  def hasCycle(self, head: ListNode) -> bool:
    
    # Initialization
    d={}
    ptr=head
    
    # Travelling along the LinkedList to the end
    while ptr != None:      
      
      # Found cycle
      #if d[ptr] == 1:
      if ptr in d:
        return True
        
      d[ptr] = 1
      ptr=ptr.next
    
    # ptr reaches the end, found no cycle
    return False
    
#===========================================================
# Solution#3: Set
class Solution:
  def hasCycle(self, head: ListNode) -> bool:
    
    s = set() 
    node = head		
        
    while node:              
    
      if node in s:
        return True     
        
      s.add(node)
      node = node.next
      
    return False
    
    
    
    
    
