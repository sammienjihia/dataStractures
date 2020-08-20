"""
References: https://www.youtube.com/watch?v=k4y5Pr0YVhg
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.cache = {}
        self.coins = coins
        
        return self.makeChange(amount, 0)
    
    def makeChange(self,amount, index):
        
        if "amount{}index{}".format(amount,index) in self.cache:
            return self.cache["amount{}index{}".format(amount,index)]
        
        # base cases 
        if amount == 0:
            return 1
        
        if amount < 0:
            return 0
        num_combs = 0
        for i in range(index, len(self.coins)):
            coinChange = amount-self.coins[i] 
            result = self.makeChange(coinChange,i)
            self.cache["amount{}index{}".format(coinChange,i)] = result
            num_combs += result
        return num_combs
            
        
        
        
                    

if __name__ == "__main__":
    sol = Solution()     
    print(sol.change(4, [1,2]) )     
    
        
        