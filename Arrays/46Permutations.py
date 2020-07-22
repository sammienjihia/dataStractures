"""
Resources used:

Youtube https://www.youtube.com/watch?v=KukNnoN-SoY

"""

class Solution:
    def permute(self, nums):
        self.ans_arr = []
        
        self.calculate(nums, []) # first iteration: Arguments shall be all possible moves, and an empty list for the ans 
        
    def calculate(self, possible_moves, ans):
        # base case
        if not len(possible_moves):
            # if we are out of possible moves, add ans to ans array and reset ans array

            self.ans_arr.append(ans)
            print(self.ans_arr)
        
        for i in range(len(possible_moves)): # remove the item on the ith position and append it to the ans array.
            # what remains are the possible_moves i = 0, possible_moves = [2,3], ans = [1]
            # i = 1, possible_moves = [1,3] ans = [2]
        
            # if there are still possible moves, continue constracting the ans and 
            # decreamenting the possible moves
            x = possible_moves[:i] + possible_moves[i+1:] # include everything before the and after the ith item
            y = ans + [possible_moves[i]] # don't mutate the function's arguments, instead make copies
            self.calculate(x, y)


if __name__ == "__main__":
    sol = Solution()
    sol.permute([1,2,3])