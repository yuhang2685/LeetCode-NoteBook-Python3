# 122. Best Time to Buy and Sell Stock II
#
# Note the solutions are from the standard solutions and "Discuss".
#
#=======================================
# Solution#1 Day Trade
#=======================================
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
        return maxProfit
        
#=======================================
# Solution#2 Day Trade
#=======================================

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profits, i = 0, 0
        
        while i < len(prices):
            
            # Find next local minimum
            while i < len(prices)-1 and prices[i+1] <= prices[i]:
                i += 1
            
            min = prices[i]
            # need increment to avoid infinite loop for "[1]"
            i += 1
            
            # Find next local maximum
            while i < len(prices)-1 and prices[i+1] >= prices[i]:
                i += 1
            
            if i < len(prices):
                profits += prices[i] - min
                
            i+=1
                
        return profits
            
