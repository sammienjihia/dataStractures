# create a class that will represent A node
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, node): # handles the complexities of node insertions
        # scenario 1. the inserted node's data is greater than the current node's val
        if node.val > self.val: # push it to the right of the current node
            # check for a right child
            if self.right:
                return self.right.insert(node)
            else:
                self.right = node
                return True
        # scenario 2. the inserted node's data is equal to the current node's val
        if node.val == self.val:
            return False
        # scenario 3. the inserted node's data is smaller than the current node's val 
        if node.val < self.val: # push it to the left of the current node
            # check for a left child
            if self.left:
                return self.left.insert(node)
            else:
                self.left = node
                return True



# create a class to represent a tree
class Tree:
    def __init__(self):
        self.root = None

    """
    The insert function takes in the data to be inserted to the tree. It acts as an interface
    """
    def insert(self, data):
        if self.root: # check if the tree already has a root node
            return self.root.insert(Node(data))

        else:
            # if the tree doesn't have a root node, the initialize a new node and make it the tree's
            # root node
            self.root = Node(data)

            return True

bst = Tree()

for item in [5,4,6,3,5,1,2]:
    print(bst.insert(item))
