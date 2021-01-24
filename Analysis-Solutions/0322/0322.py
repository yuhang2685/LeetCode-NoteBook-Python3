# 0322. Coin Change
#
# Note:
# In "Solution#1 Dynamic Programming - Time Limit Exceeded" due to not fully storing computation results.
# In "Solution#1 Dynamic Programming - Correct", we added two codes to store the failure computations, they worked.
#
#========================================================
# Solution#1 Dynamic Programming - Time Limit Exceeded
#========================================================
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def __init__(self):
        self.d = {}
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in self.d:
            return self.d[amount]
        
        if amount == 0:
            return 0
        if amount < min(coins):
            return -1
        if amount in coins:
            self.d[amount] = 1
            return 1
        # amount > min(coins)
        # Calc min coins counter for sub-problems
        min_cnt = 10000000
        for i in coins:
            sub = self.coinChange(coins, amount-i)
            if sub == -1:
                continue
            else:
                min_cnt = min(sub, min_cnt)
        if min_cnt == 10000000:
            return -1
        else:
            self.d[amount] = 1 + min_cnt
        return 1 + min_cnt

#========================================================
# Solution#1 Dynamic Programming - Correct
#========================================================
class Solution:
    
    def __init__(self):
        self.d = {}
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in self.d:
            return self.d[amount]
        
        if amount == 0:
            return 0
        if amount < min(coins):
            return -1
        if amount in coins:
            self.d[amount] = 1
            return 1
        
        # amount > min(coins)
        # Calc min coins counter for sub-problems
        min_cnt = 10001
        for i in coins:
            sub = self.coinChange(coins, amount-i)
            if sub == -1:
                self.d[amount] = -1
                continue
            else:
                min_cnt = min(sub, min_cnt)
        if min_cnt == 10001:
            self.d[amount] = -1
            return -1
        else:
            self.d[amount] = 1 + min_cnt
        return self.d[amount]
    
    
    
    
        
