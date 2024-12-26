def checkIfPossible(n, prerecs):
    
    def build_adj_indegree(n, prerecs):
        adj_list =[[] for _ in range(n)]
        indegree = [0]*n

        for prerec in prerecs:
            to_Take, take_this_first = prerec[0], prerec[1]

            adj_list[take_this_first].append(to_Take)
            indegree[to_Take]+=1
        
        return [adj_list, indegree]

    visited={}
    stack=[]
    count=0
    
    graph, indgree=build_adj_indegree(n, prerecs)

    for i in range(n):
        if indgree[i]==0:
            stack.append(i)

    while stack:
        curr= stack.pop()
        visited[curr]=True
        count+=1

        neighbours=graph[curr]

        for neighbour in neighbours:
            indgree[neighbour] -=1
            if indgree[neighbour] == 0:
                stack.append(neighbour)

    return count==n

n=8
prerecs1=[[1,0],[2,0],[4,2],[3,2],[1,3],[5,6],[7,5],[7,6]]
prerecs2=[[1,2], [2,3], [3,1]]
print(checkIfPossible(n, prerecs1))
print(checkIfPossible(n, prerecs2))