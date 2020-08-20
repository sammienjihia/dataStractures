"""
A stack is a limited access data structure. This means elements can be added or removed from the stack 
only at the top. It follows the first in, last out principle.
Two operations are allowed, push adds an item at the top and pop removes an item from the top.

Applications:
1. Check if a word is a palindrome
2. check if a string of brackets is balances
3. Undo operation in a text editor. This operation is achieved by adding all text operations to a stack
4. Backtracking; where you need to access the most recent elements in a series of elements. Example is a maze.
if you reach a dead end, you need to back track to where you came from.

Implementation:
A stack can be considered an adapter class, basically built on top of another data structure. The underlying 
structure could be an implementation of any collection.

Resource used: https://www.cs.cmu.edu/~adamchik/15-121/lectures/Stacks%20and%20Queues/Stacks%20and%20Queues.html

"""

class Stack:
    def __init__(self, collection):
        self.myStack = []

        for item in collection:
            self.myStack.append(item)

    def push(self, item):
        """
        This method inserts an item to a stack. It takes a time complexity of O(1) since 
        it's a single operation
        """
        self.myStack.append(item)

    def peek(self):
        """
        This operation returns the item on top of the stack. I takes a time complexity of O(1)
        """
        return self.myStack[-1]

    def popStack(self):
        """
        This operation removes and returns the item on top of the stack. It takes a time complexity of O(1)
        """
        return self.myStack.pop()


# Solution brute force
class Solution:
    def peek(self, stack):
        if len(stack) == 0:
            return False
        else:
            return stack[-1]
        
    def isValid(self, s: str) -> bool:
        myStack = []
        openingChar = ["(", "{", "["]
        completeTags =  {
            ")": "()",
            "]": "[]",
            "}": "{}"
        }
        for char in s:
            if char in openingChar:
                myStack.append(char)
                
            else:
                # evaluate if whats on top of stack and what's in the string form
                # a complete tag
                temp = self.peek(myStack) # peek
                if temp == False:
                    return temp
                if (temp+char) == completeTags[char]:
                    myStack.pop()
                    
                else:
                    return False
        if len(myStack) == 0:
            return True

set()
# Optimized solution
class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        completeTags =  { ")": "(", "]": "[", "}": "{" }
        for char in s:
            if char in "({[":
                myStack.append(char)  
            else:
                if myStack and completeTags[char] == myStack[-1]:
                    myStack.pop()
                else:
                    return False
        if not myStack:
            return True
        else:
            return False
                
            
            
        
            
        