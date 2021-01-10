# 0206. Reverse Linked List
#
# NOTE:
#
# Solution#1 is intuitive, but it can be more concise if we use "head" instead of "p".
#
# Solution#2 is recursion, we start with a base case "head is None".
# Then we work on the inductive cases, 
# but found "head.next is None" is hard to work with in the inductive cases,
# therefore we move it to the base cases.
#
# The inductive cases are still tricky.
# We work with an example 3->4->5 to figure out the work.
# Generally speaking, the inductive cases work by "decomposing - recomposing". 
# That is, we decompose the component into the next lower level components, 
# pretend the sub-components are handled correctly, and then "combining" them correctly.
#
# Back to the task, the inductive case is given a component "l_1" to return "reversed l_1". 
# The input-output-functionality is same as the whole problem, but work with the partial.
# First, decompose l_1 into sub-components "head_1" (that is for reasoning, but we still use "head" in the code) and "l_2", 
# then hold head_1 in hand and throw l_2 into the recursion and pretend it returns l_2' which is the "reversed l_2".
# Next, how to combine head_1 and l_2'?
# Note we can not travel to the end of l_2' to add head_1. 
# By looking at examples, we noticed the end of l_2' is always head_1.next. We can refer to it by denote it as "end".
# Now we can add head_1 to "end".
# Also remember head_1 still points to its own next as beginning, we need to change it to "None".

#==========================================
# Solution#1 Iteratively
#==========================================
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
      
      rst = None
      p = head
      
      while p:
      
        copy = p
        p = p.next
        
        copy.next = rst 
        rst = copy
        
      return rst

#==========================================
# Solution#2 Recursively
#==========================================
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
    
      # base cases
      if head == None:
        return None
        
      if head.next == None:
        return head
      
      # inductive cases
      if head.next != None:
        p = self.reverseList(head.next)    
        end = head.next
        end.next = head
        
        head.next = None
        return p
