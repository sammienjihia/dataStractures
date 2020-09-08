"""
Properties of a binary search tree are. every item on the left of the root node must be smaller  while every item
on the right side must be greater than the root node.
A node represents a single item in the tree.
A node shall contain the value of the node and/or the values of the right or the left children
A tree represent the collection of all the items in the tree.
Operations to be performed on the tree are insertion, search.
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

        


if __name__ == "__main__":
    items = [5,2,6,4,1]
    bst = Tree()
    for item in items:
        print(bst.insert(item))






