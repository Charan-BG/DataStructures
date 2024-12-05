"""
Minimum Time to Rot All
Last Updated : 17 Sep, 2024
Given a matrix of dimension M * N, where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:  

0: Empty cell
1: Cells have fresh oranges
2: Cells have rotten oranges
The task is to the minimum time required so that all the oranges become rotten. A rotten orange at index (i,j ) 
can rot other fresh oranges which are its neighbors (up, down, left, and right). If it is impossible to rot every 
orange then simply return -1.
"""
from collections import deque
def min_time_to_rot_all_oranges(grid):
    row, col = len(grid), len(grid[0])
    queue=deque()
    fresh_count=0

    for i in range(row):
        for j in range(col):
            if grid[i][j]==2:
                queue.append((i, j, 0))
            elif grid[i][j]==1:
                fresh_count+=1

    directions=[(-1,0), (1,0), (0,-1), (0, 1)]
    max_time=0
    
    while queue:
        x, y, time= queue.popleft()
        max_time=max(max_time, time)
        for dx, dy in directions:
            nx, ny= x+dx, y+dy

            if 0<=nx<row and 0<=ny<col and grid[nx][ny]==1:
                grid[nx][ny]=2
                fresh_count-=1
                queue.append((nx, ny, time+1))

    return max_time if fresh_count==0 else -1



# Test Cases
grid1 = [[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]]
grid2 = [[2, 1, 0, 2, 1], [0, 0, 1, 2, 1], [1, 0, 0, 2, 1]]

print(min_time_to_rot_all_oranges(grid1))  # Output: 2
print(min_time_to_rot_all_oranges(grid2))  # Output: -1



"""
[2, 1, 0, 2, 1],
[1, 0, 1, 2, 1],
[1, 0, 0, 2, 1]

[2, 1, 0, 2, 1],
[0, 0, 1, 2, 1],
[1, 0, 0, 2, 1]
"""