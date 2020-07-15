"""
The breadth first search tree/graph traversal basically implements a FIFO queue.
This means we explore the nodes level by level
"""

graph = {
    "A": ['B','C'],
    "B": ['D', 'E'],
    "C": ['F'],
    "D": [],
    "E": ['F'],
    "F": []
}

visited = set()
nodeQueue = []

def bfs(node):
    # add node to queue
    nodeQueue.append(node)

    while len(nodeQueue):
        # dequeue node 
        node = nodeQueue.pop(0) # FIFO queue, first in first out

        # check if the node has already been visited
        if node not in visited:
            print(node)
            # if it yes to be visited, then mark it as visited
            visited.add(node)

            # explore it's neighbours
            for neighbour in graph[node]:
                # add neighbour to queue
                nodeQueue.append(neighbour)

if __name__ == "__main__":
    bfs("A")