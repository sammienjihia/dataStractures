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

# create a BST
bst = Tree()
items = [5,3,6,1,4,7,8,9,2,0]

for item in items:
    print(bst.insert(item))


##############################################
#                                            #
#           INODER TRAVERSAL                 #
##############################################
ml = []
def inOrderTraversal(root_node):
    
    if root_node == None:
        return
    inOrderTraversal(root_node.leftchild)
    ml.append(root_node.val)
    inOrderTraversal(root_node.rightchild)

    return ml
print(inOrderTraversal(bst.root))

def inOrderTraversalIterative(root_node):
    my_stack = [] # add to stack all the left children of the tree.

    my_stack.append(root_node)

    # first step is to add the root's left child/children
    while root_node or len(my_stack):
        root_node = root_node.leftchild if root_node != None else root_node
        if root_node == None and len(my_stack):
            # pop the stack, print it and make the right child of the current root node to be the root_node
            node = my_stack.pop()
            print(node.val)
            root_node = node.rightchild
            if root_node:
                my_stack.append(root_node)

        elif root_node != None:
            my_stack.append(root_node)
       
inOrderTraversalIterative(bst.root)