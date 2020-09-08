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
def postOrderTraversal(root_node):
    if root_node == None:
        return 
    postOrderTraversal(root_node.leftChild)
    postOrderTraversal(root_node.rightChild)
    ml.append(root_node.val)
    return ml
    
print(postOrderTraversal(bst.root))