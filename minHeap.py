"""
A python implementation of the minimum priority queue or simply a minimum heap 
Operations to be performed are
1. Push: Inserting an item into the queue
2. Bubble Up: Moving inserted item to the required position based on it's priority
3. Pop: Removing an item from the queue
4. Bubble down: Moving item to be removed accross the queue
5. Peek: check item in at the top of the heap
"""
# The class can be initialised with a list of items
class MinHeap:
    def __init__(self, items=[]):
        self.heap=[0] # A list representation of the heap. NB: the 0th index of the list has been assigned

        # if the class has been initialised with a list of items, then create the heap
        for item in items:
            self.heap.append(item)

            # internal function to move the inserted item to it's position in the priority queue
            self._bubbleUp(len(self.heap)-1)

    """
    This function basically takes the last index in the heap, and calculates the index of the parent node
    """
    def _bubbleUp(self, index):
        ChildNode_index = index
        parentNode_index = index//2

        if index <=1: # this denotes we are at the root of the heap or out of index
            return

        while self.heap[ChildNode_index] < self.heap[parentNode_index]: # whenever the child node is smaller than the root node, then perform a swap
            # swap
            self._swap(ChildNode_index, parentNode_index)
            # make the parentNode_index the new childNode_index
            # take care of the out of index exception being thrown
            temp = ChildNode_index
            ChildNode_index = parentNode_index
            parentNode_index = temp//2

            # take care of the index out of bound exception
            if parentNode_index < 1:
                return

    """
    This private function is used to swap the nodes 
    """
    def _swap(self, ChildNode_index, parentNode_index):
        self.heap[ChildNode_index], self.heap[parentNode_index] = self.heap[parentNode_index], self.heap[ChildNode_index]

x = MinHeap([5,3,1,2,8])
print(x.heap)






