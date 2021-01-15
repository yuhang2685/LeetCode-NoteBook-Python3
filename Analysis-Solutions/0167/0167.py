# 167. Two Sum II - Input array is sorted
#
# Note:
# Solution#1 is based on the property that the array is sorted. It is a little tricky. It is fast.
# The idea is with looking at pt1 and pt2: 
# if their sum is too big, we hold pt1 and try reducing pt2 with its content, (why not reducing pt1? because it has already been checked)
# if their sum is too small, we hold pt2 and try increasing pt1 with its content, (why not increasing pt2? because it has already been checked)
#
# Note for Solution#2:
# It is also based on the property that the array is sorted.
# It always returns by pointing at the bigger number and found the smaller paired number is already in the Dictionary,
# since by that time looking at the bigger number, the numbers smaller than it should have been visited and stored.
# Also be aware of Python method "enumerate" for an array, whose return pairs indexed starting from 1.
# The property makes the main difference of HT solution to 0001. "Two Sum" where it requiers two loop through the array because it might not be sorted.
#
# Note for Solution#3:
# It has two nested loops:
# The outter loop for individual number i,
# the inner loop starting from the next element of i and looks for its pair in the rest of array by using Binary Search which is faster.
#====================================
# Solution#1 - Two Pointers
#====================================
def twoSum1(self, numbers, target):
    l, r = 0, len(numbers)-1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1]
        elif s < target:
            l += 1
        else:
            r -= 1
             
#====================================
# Solution#2 - Dictionary     
#====================================
def twoSum2(self, numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target-num in dic:
            return [dic[target-num]+1, i+1]
        dic[num] = i


#====================================
# Solution#3 - Binary Search      
#====================================       
def twoSum(self, numbers, target):
    for i in xrange(len(numbers)):
        l, r = i+1, len(numbers)-1
        tmp = target - numbers[i]
        while l <= r:
            mid = l + (r-l)//2
            if numbers[mid] == tmp:
                return [i+1, mid+1]
            elif numbers[mid] < tmp:
                l = mid+1
            else:
                r = mid-1        
