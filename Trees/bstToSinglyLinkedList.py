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

"""
To create a bst we can utilize the inorder traversal utility.
Basically create an inorder traversal function that takes in the root of a bst.

NB: A linked list node has the following properties
Head of a linked list...in this scenario, it should be a global property
Node.val
Node.next -> points to either another node or None if it's the tail node

"""
class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class BstToLl:

    def __init__(self):
        self.head = None
        self.currentNode = None # we have to keep track of where we are within the linked list

    def bstToLinkedlist(self, bst_root, bst_root2):
        head1 = self.inOrderTraversal(bst_root)
        head2 = self.inOrderTraversal(bst_root2)

        merged_head = None # this is the head of the newly created linked list
        temp = None # keeps track of the last node in the newly created linked list

        # Check if we have both heads of the two linked lists
        if not head1:
            return head2
        if not head2:
            return head1

        curr1 = head1
        curr2 = head2

        while curr1 and curr2:
            # check if the newly created linked list has a head
            if not merged_head:
                if curr1.val <= curr2.val:
                    temp = curr1
                    merged_head = temp
                    curr1 = curr1.next
                else:
                    temp = curr2
                    merged_head = temp
                    curr2 = curr2.next

            else:
                if curr1.val <= curr2.val:
                    temp.next = curr1
                    temp = curr1
                    curr1 = curr1.next

                else:
                    temp.next = curr2
                    temp = curr2
                    curr2 = curr2.next

        # handle scenrio where we've reached the end of only one linked list
        if not curr1:
            temp.next = curr2
        if not curr2:
            temp.next = curr1
        return merged_head

    def inOrderTraversal(self, root):
        if root == None:
            return
        self.inOrderTraversal(root.leftChild)
        LLhead = self.createLL(root)
        self.inOrderTraversal(root.rightChild)
        return LLhead

    def createLL(self, bstnode): # this function shall return the head of the linked list
        # create a linked list node from the node of a bst
        lnode = LinkedListNode(bstnode.val)
        if self.head == None:
            # if the head node is none, then create a node and make it the head
            lnode.next = None
            self.head = lnode
            self.currentNode = lnode

        else:
            self.currentNode.next = lnode
            lnode.next = None
            self.currentNode = lnode

        return self.head


        
        
        


if __name__ == "__main__":
    items = [5,2,6,4,1]
    bst = Tree()
    for item in items:
        print(bst.insert(item))

    s = BstToLl()
    print(s.inOrderTraversal(bst.root))






