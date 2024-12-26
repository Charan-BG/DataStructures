"""
Question 1:BFS - Adj List and Adj Matrix

You are given an undirected graph stored

1.as an adjacency list

2.as an adjacency Matrix.

Write functions to traverse this graph using the Breadth first Search approach. 
As you traverse the graph store the values of the vertices
"""
# TC=O(V+E) V is atleast 1(once) all vertices/node goes into queue, E edges or neighbours of a Vertix/node
# SC=O(V) space like queue, output, vertix use V len so it is (3V) if we ignore constant we get V   

def BFS_list(graph, start):
    visited={}
    visited[start]=True
    queue=[start]
    output=[]

    while queue:
        current = queue.pop(0)
        output.append(current)

        neighbours=graph[current]
        for neighbour in neighbours:
            if neighbour not in visited:
                visited[neighbour]=True
                queue.append(neighbour)

    return output



adjacency_list = {
    'A': ['B', 'F'],
    'B': ['A', 'F', 'C'],
    'C': ['B', 'E', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'C', 'F'],
    'F': ['A', 'B', 'E']
}

print(BFS_list(adjacency_list, 'A'))

#TC=O(V^2) since V is for all ele atleast once in queue, and the for to calcu.. neighbours in worst case is V
# SC=O(V) 

def BFS_Matrix(graphs, start):

    vertices=['A', 'B', 'C', 'D', 'E', 'F']
    vertices_idx={'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}

    visited={}
    visited[start]=True
    queue=[start]
    output=[]

    while len(queue)>0:
        current = queue.pop(0)
        output.append(current)

        neighbour=graphs[vertices_idx[current]]
        for i in range(len(neighbour)):
            if neighbour[i]==1 and vertices[i] not in visited:
                visited[vertices[i]] = True
                queue.append(vertices[i])
    
    return output


adjacency_matrix = [
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 0]
]

print(BFS_Matrix(adjacency_matrix, "A"))