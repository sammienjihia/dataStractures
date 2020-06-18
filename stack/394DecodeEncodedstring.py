class Solution:
    def decodeString(self, s):
        # we need to keep track of two stacks
        # 1. The alphabetical chars stack
        # 2. The nums stack

        # there are 4 possibilities to check for
        # 1. If char is a digit
        # 2. If char is an opening [
        # 3. If char is a closing ]
        # 4. If char is an alphabet

        index = 0 # to be used to iterate the string
        alphStack = [] # to be used to track the alphabets
        numStack = [] # to be used to track the numbers

        currentString = "" # Keeps track on the string we are building

        # iterate the string
        while index < len(s):

            if s[index].isdigit():
                num = 0
                # the digit can be of different value 100, 10,1
                while s[index].isdigit():
                    num = num * 10 + int(s[index])

                    # increament the index
                    index += 1
                # add the num to the numStack
                numStack.append(num)
            
            elif s[index] == '[':
                # whenever we get to an [ bracket, we should
                # add our current string the the stringStack
                alphStack.append(currentString)

                # reset currentString
                currentString = ""

                #increament index
                index += 1

            elif s[index] == ']':
                # whenever we get to a ] bracket we should pop
                # both the stacks

                # we should repeat the currentString based on the 
                # whats popped from the numStack 
                temp = alphStack.pop()

                for x in range(numStack.pop()):
                    # add the current string x amount of times
                    # from whats poped from the alphStack
                    temp = temp + currentString

                # build out the current string
                currentString = temp

                # increament index
                index += 1

            else:
                currentString += s[index]

                # increament index
                index += 1

        return currentString




if __name__ == "__main__":
    l = Solution()
    print(l.decodeString("3[a2[bc]]"))