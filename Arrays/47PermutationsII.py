class Solution:
    def permuteUnique(self, nums):
        # secret to this is to ensure not to calculate simillar consecutive digits
        
        # we are returning a list, so initialise one
        self.ans_arr = []
        
        # call our recursive function
        nums.sort()
        self.calculate(nums, [])
        
        return self.ans_arr
    def permute(self, index, possible_moves, ans):
        moves = possible_moves[:index] + possible_moves[index+1:]
        current_ans = ans + [possible_moves[index]]
        self.calculate(moves,current_ans)
    
    def calculate(self, possible_moves, ans):
        """
        For every item in the nums list we pop an item from the list
        to continually construct our ans. The remaining item in the list will be 
        our possible moves, which we shall feed to our recursive function
        """
        
        # base case
        # check if there any possible moves, if not append ans to ans arr and exit from the function
        if not len(possible_moves):
            self.ans_arr.append(ans)
            
        for i in range(len(possible_moves)):
            
            # note simillar digits in consequtive fashion shall produce same possible moves
            # hence no need to repeat
            
            # check if previous item in possible moves is simillar to current
            if i != 0 and possible_moves[i-1] != possible_moves[i]:
                self.permute(i, possible_moves, ans)
                
            elif i == 0:
                self.permute(i, possible_moves, ans)
                
            
if __name__ == "__main__":
    sol = Solution()
    print(sol.permuteUnique([3,3,0,3]))
                
                
                
                
                
                
                
                
                