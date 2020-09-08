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
    

def levelOrderTraversal(root_node):
    fifo_queue = []
    if root_node == None:
        return

    else:
        fifo_queue.append(root_node)

        while len(fifo_queue) != 0: # while the queue is not empty, pop it and save it's children
            node = fifo_queue.pop(0)
            print(node.val)
            if (node.leftChild):
                fifo_queue.append(node.leftChild)
            if (node.rightChild):
                fifo_queue.append(node.rightChild)


levelOrderTraversal(bst.root)

