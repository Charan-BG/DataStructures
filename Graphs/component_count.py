"""
Question 1:Number of connected components

You are given a graph with n vertices. To indicate the connections in the graph you are given 
an array edges whose each element is an array of the form [u,v]. [u,v] indicates that there is an 
edge between u and v where u and v denote two vertices or nodes. Write a function that takes in 
'n' and the 'edges' array and returns the number of connected components in the graph.
"""

def count_component(n, edges):
    
    count=0

    def build_adj(n, edges):
        adj_list=[[] for _ in range(n)]

        for edge in edges:
            node1=edge[0]
            node2=edge[1]

            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        return adj_list
   
    def dfs(graph, vertex, visited):
        
        visited[vertex]=True
        
        neighbours=graph[vertex]

        for neighbour in neighbours:
            if neighbour not in visited:
                dfs(graph, neighbour, visited)


    #build graph
    graph=build_adj(n, edges)
    print(graph)

    visited={}

    for vertex in range(n):
        if vertex not in visited:
            count+=1
            dfs(graph, vertex, visited)

    return count



n=7
edges1=[[0,1], [1,2], [3,4], [5,6]]
edges2=[[0,1], [1,2], [3,4]]
print(count_component(n, edges1))
print(count_component(n, edges2))