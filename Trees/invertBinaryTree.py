"""
Inverting a binary tree simply means creating a mirror of the binary tree. basically swap the left and right 
children.
Inverting a tree basically follows a postorder traversal
"""

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
            # check whether the node has a left child
            if self.leftChild:
                self.leftChild.insert(node)
            else:
                self.leftChild = node
        else:
            # check whether the node has a right child
            if self.rightChild:
                self.rightChild.insert(node)
            else:
                self.rightChild = node

        return True

    def search(self, node):
        if self.val == node.val:
            return True
        elif node.val > self.val:
            if self.rightChild:
                return self.rightChild.search(node)
            else:
                return False
        elif node.val < self.val:
            if self.leftChild:
                return self.leftChild.search(node)
            else:
                return False
        else: 
            return False

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

    def search(self, data):
        if self.root.val == data:
            return True
        else:
            return self.root.search(Node(data))

def invertTree(root):
    if root == None:
        return
    invertTree(root.leftChild)
    invertTree(root.rightChild)

    root.left, root.right = root.right, root.left
    return root



if __name__ == "__main__":
    items = [5,2,6,4,1]
    bst = Tree()
    for item in items:
        print(bst.insert(item))







