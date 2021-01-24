 # 0075. Sort Colors
 #
 # Solution#1 has two pass, O(n) time and O(1) space.
 # Solution#2 has two pass, O(n) time and O(1) space. It is interesting and done by me. The code is concise with a same efficiency as #1.
 # Solution#3 has one pass, O(n) time and O(1) space. It is from other people solution, called "dutch partitioning problem".
 # The main idea Solution#3 is: 
 # p_2 travels through the array one by one, while p_1 and p_3 stay for filling whatever p_2 found.
 # We don't need to worry about whites, whenever read and blue are correctly placed, the rest are all whites.
 # That is, whereever p_2 is at, the red and blue it has seen were placed correctly, 
 # with un-cared places are all whites because whites are left in array by p_2 skipping. 
 #=========================
 # Solution#1 - Two Pass
 #=========================
 class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue, p = 0, 0, 0, 0
        
        for i in range(len(nums)):
            
            if nums[i] == 0:
                red += 1                            
            else:
              if nums[i] == 1:
                white += 1                
              else:
                blue += 1        
        
        s = p
        p += red        
        while red > 0:
            nums[s + red - 1] = 0
            red -= 1
            
        s = p
        p += white
        while white > 0:
            nums[s + white - 1] = 1
            white -= 1
        
        s = p
        p += blue
        while blue > 0:
            nums[s + blue - 1] = 2
            blue -= 1
            
        return 

#==========================
# Solution#2 - Two pass 
#==========================
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        
        # phase_1: move all 0 to the front
        p_1, p_2 = 0, len(nums)-1
        while p_1 < p_2:
            if nums[p_2] == 0:
                nums[p_1], nums[p_2] = nums[p_2], nums[p_1]
                p_1 += 1
            else:
                p_2 -= 1
               
        # phase_2: move all 2 to the end
        p_1, p_2 = 0, len(nums)-1
        while p_1 < p_2:
            if nums[p_1] == 2:
                nums[p_1], nums[p_2] = nums[p_2], nums[p_1]
                p_2 -= 1
            else:
                p_1 += 1

        return

#==========================
# Solution#3 - One pass 
#==========================   
 class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        
        p_1, p_2, p_3 = 0, 0, len(nums)-1
        
        while p_2 <= p_3:
            
            if nums[p_2] == 1:
                p_2 += 1
            
            else:
                if nums[p_2] == 0:
                    nums[p_2], nums[p_1] = nums[p_1], nums[p_2]
                    p_1 += 1
                    p_2 += 1
                else:
                    nums[p_2], nums[p_3] = nums[p_3], nums[p_2]
                    p_3 -= 1
        return   
    
