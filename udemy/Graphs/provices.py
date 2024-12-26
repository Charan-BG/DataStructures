def findCircleNum(isConnected):
    def dfs(city):
        """Perform DFS to mark all cities in the same province as visited."""
        for neighbor, is_connected in enumerate(isConnected[city]):
            # print(neighbor, isconnected)
            if is_connected and neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)
    
    n = len(isConnected)
    visited = set()
    provinces = 0
    
    for city in range(n):
        if city not in visited:
            dfs(city)
            provinces += 1  # Found a new province
    
    return provinces



isconnected=[[1,1,0], [1,1,0], [0,0,1]]
print(findCircleNum(isconnected))
# for neighbor, is_connected in enumerate(isconnected[0]):
    # print(neighbor, isconnected)