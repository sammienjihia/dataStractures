# create a binary tree
class Node:
    def __init__(self, val):
        self.val = val
        self.rightchild = None
        self.leftchild = None

    def insert(self, node):
        # compare the data val of the nodes
        if self.val == node.val:
            return False
        if self.val > node.val: # make the new node the left child of this 
            if self.leftchild: # check if the left child has a left child
                self.leftchild.insert(node)
            else:
                self.leftchild = node

        else:
            if self.rightchild:
                self.rightchild.insert(node)
            else:
                self.rightchild = node
        return True

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root: # Check whether the tree has a root node
            return self.root.insert(Node(data))
        else: # if it doesn't make it the root node
            self.root = Node(data)
            return True

def maxDepth(root):
    if root == None:
        return 0 # If Node is None, then return 0 since it does not signify a valid depth
    left = maxDepth(root.leftchild)
    right = maxDepth(root.rightchild)

    return max(left, right)+1 # we add 1 to the max for the current node

# create a BST
bst = Tree()
items = [5,3,6,1,4,7,8,9,2,0]

for item in items:
    print(bst.insert(item))

assert(maxDepth(bst.root) == 5 )