class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None
    def insert(self, node):
        # this function shall decide on whether the node shall be a left child or a right child
        if self.val == node.val:
            return False
        if self.val > node.val:
            # check whether the node has children
            if self.leftChild:
                self.leftChild.insert(node)
            else:
                self.leftChild = node
        else:
            if self.rightChild:
                self.rightChild.insert(node)
            else:
                self.rightChild = node

        return True

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # check if root node is present
        if self.root:
            return self.root.insert(Node(data))
        else:
            self.root = Node(data)
            return True

    def constructTree(self,items):
        for item in items:
            self.insert(item)

items = [5,3,6,1,4,7,8,9,2,0]
bst = Tree()
for item in items:
    print(bst.insert(item))

ml = []   
def preOrderTraversal(root_node):
    if root_node == None:
        return

    ml.append(root_node.val)
    preOrderTraversal(root_node.leftChild)
    preOrderTraversal(root_node.rightChild)
    return ml


print(preOrderTraversal(bst.root))

"""
NB: Before adding a node to a stack, print the node.
NB after poping stack, get the right child of the poped node. This is because if a node has been inserted to
the stack, then it means we've already seen it's leftchild

"""
def preOrderTraversalIterative(root_node):
    my_stack = []
    my_stack.append(root_node)
    print(root_node.val)

    while root_node or len(my_stack):
        root_node = root_node.leftChild if root_node != None else root_node
        if root_node == None and len(my_stack):
            # if root is none, 
            # 1. then pop stack, 
            # 2. get the right child of the node and 
            # 3. make it the new root
            # 4. then add it to stack
            # 5. Print the root 
            node = my_stack.pop()
            root_node = node.rightChild
            if root_node:
                my_stack.append(root_node)
                print(root_node.val)
        else:
            my_stack.append(root_node)
            print(root_node.val)

preOrderTraversalIterative(bst.root)