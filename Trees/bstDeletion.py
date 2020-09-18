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

    def search(self, node):
        if self.val == node.val:
            return True
        elif node.val > self.val:
            if self.rightchild:
                return self.rightchild.search(node)
            else:
                return False
        elif node.val < self.val:
            if self.leftchild:
                return self.leftchild.search(node)
            else:
                return False
        

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root: # Check whether the tree has a root node
            return self.root.insert(Node(data))
        else: # if it doesn't make it the root node
            self.root = Node(data)
            return True

    def search(self, data):
        if self.root.val == data:
            return True
        else:
            return self.root.search(Node(data))

# create a BST
bst = Tree()
items = [5,3,6,1,4,7,8,9,2,0]

for item in items:
    print(bst.insert(item))

ml = []
def inOrder(root_node):
    if root_node == None:
        return 
    inOrder(root_node.leftchild)
    ml.append(root_node.val)
    inOrder(root_node.rightchild)
    return ml
#####################################
#       Deleting a node in a BST    #
#       Case 1. Node has no child   #
#####################################

def deleteNode(data):
    isPresent = bst.search(data)
    mystack = [] # to hold all the left children of the node to be deleted right subtree

    if not isPresent:
        # the item is not in the tree
        return False
    else:
        # case 1. Node has no child
        # Get the node's predecessor
        node = bst.root

        node_predecessor = None
        node_successor_right = node.rightchild # initialize the node's successors
        node_successor_left = node.leftchild

        # if data == node.val:
        #     bst.root = None
        #     return True

        # else the root is not the node beng searched
        while node and node.val != data:
            # this is used to get the node's successor before actually reaching the Node
            node_predecessor = node # create a node successor variable to hold the parent
            # check of the node being searched is eaither greater than or less than the parent
            if data > node_predecessor.val: # search in the right
                node = node_predecessor.rightchild
                if node and node.val == data:
                    # get the successor if the node is on the right side of the root.
                    # There might be either no successor if the node doesn't have children
                    # Or one successor if the node has one child 
                    # Or two successors if the node has 2 children
                    node_successor_right = node.rightchild
                    node_successor_left = node.leftchild
            else:
                node = node_predecessor.leftchild
                if node and node.val == data:
                    # get the successor if the node is on the left side of the root
                    node_successor_right = node.rightchild
                    node_successor_left = node.leftchild
                

        
        

        # figure out if the node has both children
        if node_successor_right and node_successor_left:
            print("QQQQQQQQQQQQQQQ")
            print(node_successor_right.val)
            print(node_successor_left.val)
            # so the node to be deleted has 2 children
            # get the least node on the node's right sub-tree.
            # i'll use a while loop to get to the leaf 
            # i'll also use a stack to append the left children
            # case 1. if the right child is a leaf, then just replace it with the node to be deleted
            if node_successor_right.leftchild: # this means the right sub-tree has a minimum value
                new_node = node_successor_right.leftchild # this shall be the node to replace what is to be deleted
                mystack.append(new_node) # add it to the stack
                while new_node:
                    new_node = new_node.leftchild # get the left child of the new node
                    if new_node: # if the new_node is none, then we exit the loop
                        mystack.append(new_node)

                # when you pop the stack, you'll get the node with the least value
                new_node = mystack.pop()
                if node_predecessor:
                    if node_predecessor.rightchild.val == data: # the node to deleted is the right child of the parent/predecessor
                        node_predecessor.rightchild = new_node
                        new_node.rightchild = node_successor_right
                    else:
                        node_predecessor.leftchild = new_node
                        new_node.rightchild = node_successor_right

                else: # if the node_predecessor is none, then the node is a root node
                    # make the new node the root
                    bst.root = new_node
                    new_node.rightchild = node_successor_right


            else:
                if node_predecessor:
                    # the predecessor should point to the node successor right
                    if node_predecessor.rightchild.val == data: # the node is the right child of the parent
                        node_predecessor.rightchild = node_successor_right
                        node_successor_right.leftchild = node_successor_left
                    else:
                        node_predecessor.leftchild = node_successor_right
                        print("TTTTTTTTTTTTTTTT")
                        print(node.val)
                        print(node_successor_right.val)
                        print(node_successor_left.val)
                        node_successor_right.leftchild = node_successor_left

        # Node has only one child. The right child
        elif node_successor_right and not node_successor_left:
            if node_predecessor:
                # if the node has only one child, then it's predecessor shall point to it's successor
                if node_predecessor.rightchild.val == data: # the node is the right child of the parent
                    node_predecessor.rightchild = node_successor_right
                else:
                    node_predecessor.leftchild = node_successor_right
        # node has only one successor. The left child
        elif node_successor_left and not node_successor_right:
            if node_predecessor:
                # if the node has only one child, then it's predecessor shall point to it's successor
                if node_predecessor.rightchild.val == data: # the node is the right child of the parent
                    node_predecessor.rightchild = node_successor_left
                else:
                    node_predecessor.leftchild = node_successor_left
        # node has no successor 
        else:
            if node_predecessor:
                # if the node has no successor, then figure out if the node is the right child or the left child of the predecessor
                if node_predecessor.rightchild.val == data: # the node is the right child of the parent
                    node_predecessor.rightchild = None
                else:
                    node_predecessor.leftchild = None


    return True
     

print("########")
print("Tree before deletion")
# print(inOrder(bst.root))
print(bst.search(6))
print(bst.search(40))
x = deleteNode(5)
print("Tree after deletion")
if x:
    print("node {} has been deleted successfuly".format(4))
else:
    print("no deletion has occured")
print(inOrder(bst.root))

