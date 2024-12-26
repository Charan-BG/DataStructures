"""
Question 2:DFS - Iterative and Recursive

You are given a graph stored as an adjacency list. Write functions to traverse the graph using the Depth first Search approach
1) recursively and
2) iteratively.
As you traverse the graph store the values of the vertices in an array and return this array.
"""

def DFS_list(graphs, vertex):
    visited={}
    output=[]

    def helper(graphs, vertex, output, visited):
        
        output.append(vertex)
        visited[vertex]=True

        neighbours=graphs[vertex]

        for neighbour in neighbours:
            if neighbour not in visited:
                helper(graphs, neighbour, output, visited) 

    helper(graphs, vertex, output, visited)
    return output


# Define the adjacency list of the graph
adjacency_list = {
    'A': ['B', 'F'],
    'B': ['A', 'C'],
    'C': ['B', 'E', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'C', 'F'],
    'F': ['A', 'E']
}

print(DFS_list(adjacency_list, 'A'))
# print(DFS_list(adjacency_list, 'B'))
# print(DFS_list(adjacency_list, 'F'))


def DFS_iter(graphs, start):

    visited={}
    stack=[start]
    output=[]
    visited[start]=True

    while stack:
        current= stack.pop()
        output.append(current)

        neighbours= graphs[current]

        for neighbour in neighbours:
            if neighbour not in visited:
                stack.append(neighbour)
                visited[neighbour]=True

    return output


adjacency_list = {
    'A': ['B', 'F'],
    'B': ['A', 'C'],
    'C': ['B', 'E', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'C', 'F'],
    'F': ['A', 'E']
}

print(DFS_iter(adjacency_list, 'A'))


def DFS_matrix(graphs, start):

    vertex=['A','B','C','D','E','F']
    vertex_idx={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}

    visited={}
    stack=[start]
    output=[]
    visited[start]=True

    while stack:
        current= stack.pop()
        output.append(current)

        neighbours= graphs[vertex_idx[current]]

        for i in range(len(neighbours)):
            if neighbours[i]==1 and vertex[i] not in visited:
                stack.append(vertex[i])
                visited[vertex[i]]=True

    return output


adjacency_matrix = [
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 0]
]

print(DFS_iter(adjacency_list, 'A'))

