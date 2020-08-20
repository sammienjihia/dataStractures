"""
Dijkstra's algorithm can be considered an implementation of a BFS whereby instead of using 
a FIFO queue, we use a priority queue
"""

class dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.priority_queue = [0]

    def bubble_up(self, last_index):
        # unzip dictionary
        child_item = list(self.priority_queue[last_index].values())[0]
        parent_item = list(self.priority_queue[last_index//2].values())[0]
        if child_item >= parent_item[last_index//2]:
            return
        else:
            parent_index = last_index//2
            child_index = last_index
            self.priority_queue[child_index],self.priority_queue[parent_index] = self.priority_queue[parent_index],self.priority_queue[child_index]
            last_index = parent_index
            self.bubble_up(last_index)

    def bubble_down(self, parent_index):
        
        last_index = len(self.priority_queue)-1
        # check if the parent node is the last node in the heap
        if parent_index == last_index:
            return

        child_index_left = parent_index*2
        child_index_right = parent_index*2 + 1

        # check if there are children
        if not child_index_left  > last_index: # This means the parent has children
            # check if the parent has two children
            if child_index_right <= last_index:
                # take the smallest of the children and swap
                child_index = child_index_left if  self.priority_queue[child_index_left] <= self.priority_queue[child_index_right] else child_index_right

                if self.priority_queue[parent_index] > self.priority_queue[child_index]: # if node value of parent is greater than the selected child then swap
                    self.priority_queue[parent_index], self.priority_queue[child_index] = self.priority_queue[child_index], self.priority_queue[parent_index]
                    # then recursively call this function with the child_index being the new parent index
                    self.bubble_down(child_index)
                else:
                    return
            else:
                # parent has only one child
                # check if parent value is less than child
                if self.priority_queue[parent_index] > self.priority_queue[child_index_left]: 
                    # if parent value greater than child, then swap
                    self.priority_queue[parent_index], self.priority_queue[child_index_left] = self.priority_queue[child_index_left], self.priority_queue[parent_index]
                    # else do nothing
        else:
            return

        child_item_left = list(self.priority_queue[parent_index*2].values())[0]
        child_item_right = list(self.priority_queue[parent_index*2 + 1].values())[0]
        parent_item = list(self.priority_queue[parent_index].values())[0]

    def enQueue(self, node):
        # a node consists of a) node name b) cost to get to that node
        self.priority_queue.append(node)

        # if the len of queue is greater than 2(means we have at least 2 indices, index 0 not included), then heapify
        len_of_queue = len(self.priority_queue)
        if len_of_queue > 2:
            # heapifying is basically comparing the node to it's parent
            # if the node value is smaller than parent then swap
            self.bubble_up(len_of_queue-1)

    def deQueue(self):
        last_index = len(self.priority_queue)-1
        # swap first item and last item
        self.priority_queue[last_index], self.priority_queue[1] = self.priority_queue[1], self.priority_queue[last_index]

        # pop item from queue
        de_queued_item = self.priority_queue.pop()

        if len(self.priority_queue) > 2:
            #bubble_down
            self.bubble_down(1)# index of top most item in the min heap
        return de_queued_item

    def dijkstra_algo(self, node): # takes in the source node
        distances = {} # this dict shows rpresents the node as key and the the distance to get to the node from the source as value
        distances[list(node.keys())[0]] = list(node.values())[0]
        # add node to priority queue
        self.enQueue(node)

        while len(self.priority_queue): # while the queue still has items, process the items
            print(distances)
            # remove dequeue the priority queue
            node_to_process = self.deQueue()
            
            # check if the node has already been visited|| use the node name
            if list(node_to_process.keys())[0] not in self.visited:
                # if we haven't yet visited the node, the mark it as visited and process it
                self.visited.add(list(node_to_process.keys())[0])

                # process the neigbors
                for node in self.graph[list(node_to_process.keys())[0]]:
                    # add neibour to queue
                    list(node.values())[0] += list(node_to_process.values())[0]
                    self.enQueue(node)
                    distances[list(node.keys())[0]] = list(node.values())[0]
                    


graph = {
    "0":[{'1':3}, {'3':2}, {'8':4}],
    "1":[{'7':4}],
    "2":[{'7':2}, {'3':6}, {'5':1}],
    "3":[{'0':2},{'4':1},{'2':6}],
    "4":[{'8':8},{'3':1}],
    "5":[{'2':1}, {'6':8}],
    "6":[{'5':8}],
    "7":[{'1':4}, {'2':2}],
    "8":[{'0':4},{'4':8}]
}

priority_queue = []
visited = set()
# def dijkstra_(node):
#     # add node to priority queue
#     priority_queue.append(node)
#     distance = 0

#     while len(priority_queue):
#         # remove item from queue
#         node = priority_queue.pop(0)

#         if node.keys()[0] not in visited:
#             visited.add(node.keys()[0])

#             for neighbours in graph[node.keys()[0]]:
#                 priority_queue.append(neighbours)

#                 priority_queue.sort(key=lambda x: x.values())


#     print(visited)

if __name__ == "__main__":
    # dijkstra_({"0":0})
    d = dijkstra(graph)
    d.dijkstra_algo({"0":0})
