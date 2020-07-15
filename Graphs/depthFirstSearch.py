"""
Depth first search/ Explorative graph search utilises a stack, can be a stack that we create or
a call stack when implemented using recursion.
Explore all neighbours to a node
Depth First Search (DFS) uses the concept of backtracking at its very core.
"""

# Using a call stack/ recursion
graph = {
    "A": ['B','C'],
    "B": ['D', 'E'],
    "C": ['F'],
    "D": [],
    "E": ['F'],
    "F": []
}

visited = set()

def dfs(visited, graph, node): # utilises recursion, hence the call stack
    if node not in visited: # if we haven't visited the node, then explore it
        print(node)
        visited.add(node)
        for neighbour in graph[node]: # with recursion the loop becomes nested. We are basically exploring the neighbours
            dfs(visited, graph, neighbour)


# using a fifo queue/ 
graph2 = {
    "A": ['B','C'],
    "B": ['D', 'E'],
    "C": ['F'],
    "D": [],
    "E": ['F'],
    "F": []
}

isVisited = set()
nodeStack = []

def dfsStack(node):
    # push node to stack
    nodeStack.append(node)

    while len(nodeStack): # This condition checks 
        node = nodeStack.pop()

        # check if node has already been visited
        if node not in isVisited:
            print(node)
            # mark the node as visited 
            isVisited.add(node)

            # explore it's neighbours
            for neighbour in graph2[node]:
                # add neigbour to the stack
                nodeStack.append(neighbour)



if __name__ == "__main__":
    dfs(visited, graph, "A")
    dfsStack('A')
"""

A, B, D, E, F, C

Resources used: https://www.freecodecamp.org/news/lets-backtrack-and-save-some-queens-1f9ef6af5415/#:~:text=Depth%20First%20Search%20(DFS)%20uses,up%20in%20two%20possible%20states.

"""

