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

if __name__ == "__main__":
    mySatck = Stack([1,2,3,4,5])

    " Print the stack"
    print(mySatck.myStack)

    "Add an item to the stack"
    mySatck.push(8)

    "Print current stack"
    print("Current stack content {}".format(mySatck.myStack))

    "Peek the item on top of the stack"
    print("Item at the top of the stack is {}".format(mySatck.peek()))


    "Remove two items form the stack"
    print("Removed {} from stack. Current stack is {}".format(mySatck.popStack(), mySatck.myStack))
    print("Removed {} from stack. Current stack is {}".format(mySatck.popStack(), mySatck.myStack))