"""
Coding Exercise: 01 Knapsack
You are provided with a set of N items, each with a specified weight and value. Your objective is 
to pack these items into a backpack with a weight limit of W, "maximizing"(then its DP releated) the total value of items in
the backpack. Specifically, you have two arrays: val[0..N-1], representing the values of the items, and 
wt[0..N-1], indicating their weights. Additionally, you have a weight limit W for the backpack. The 
challenge is to determine the most valuable combination of items where the total weight does not exceed W. 
Note that each item is unique and indivisible, meaning it must be either taken as a whole or left entirely.

Input:
N = 3
W = 8
values[] = [2,3,9]  [2,3,9]
weight[] = [8,2,5]  [2,2,5]
Output: 12
Explanation: Choose the last 2 items that weighs 2 and 5 units respectively and hold values 3 and 9 that add up to 12. 
"""

"""NOTE: If knapsack_01 or unbounder knapsack is asked do the tabulation part difference is just this dp[i-1] to d[i]
include=val[i-1]+dp[i][j-wt[i-1]]"""

# Approach 1 TC=O(2^n), ST=O(n)
def knapsack(wt, val, W, N):

    def helper(i, w):
        #base case
        if i>N-1:
            return 0
        if w<=0:
            return 0 
        
        #recursive
        # for i in range(N):
        
        exclude=helper(i+1, w)
        include=0
        if wt[i]<=W:
            #include
            include = val[i]+helper(i+1, w-wt[i])

        return max(include, exclude)
    return helper(0, W)

print(knapsack([8,2,5],[2,3,9], 8, 3))
print(knapsack([2,2,5],[2,3,9], 9, 3))
print(knapsack([2,2],[5,10], 3, 2))
print(knapsack([1,2],[5,10], 3, 2))


# Approach 2 TC=O(n*w), ST=O(n*w)
def knapsack_2(wt, val, W, N):

    dp=[[-1]*(W+1) for _ in range(N)]
    def helper(i, w):
        #base case
        if i>N-1:
            return 0
        if w<=0:
            return 0 
        
        #recursive
        if dp[i][w] !=-1:
            return dp[i][w]
        
        exclude=helper(i+1, w)
        include=0
        if wt[i]<=W:
            #include
            include = val[i]+helper(i+1, w-wt[i])

        dp[i][w] = max(include, exclude)
        return dp[i][w]
    return helper(0, W)

print(knapsack_2([8,2,5],[2,3,9], 8, 3))
print(knapsack_2([2,2,5],[2,3,9], 9, 3))
print(knapsack_2([2,2],[5,10], 3, 2))
print(knapsack_2([1,2],[5,10], 3, 2))

# Approach-3 TC=O(n*w), SC=O(n*w)
def knapsack01_3(wt, val, W, N):

    dp=[[0]*(W+1) for _ in range(N+1)]

    for i in range(1,N+1):
        for j in range(1,W+1):

            exclude = dp[i-1][j]
            include=0
            if wt[i-1]<=j:
                include=val[i-1]+dp[i-1][j-wt[i-1]]
            dp[i][j] = max(exclude, include)

    return dp[N][W]

print(knapsack01_3([8,2,5],[2,3,9], 8, 3))
print(knapsack01_3([2,2,5],[2,3,9], 9, 3))
print(knapsack01_3([2,2],[5,10], 4, 2))
print(knapsack01_3([1,2],[5,10], 3, 2))

# approach-4 TC=O(n*w), SC=O(w)
def knapsack01_4(wt,val,W,N):

    prev=[0]*(W+1)
    curr=[0]*(W+1)

    for i in range(1,N+1):
        for j in range(1,W+1):

            exclude=prev[j]
            include=0
            if wt[i-1]<=j:
                include=val[i-1]+prev[j-wt[i-1]]
            curr[j]=max(exclude, include)

        prev=curr[:]

    return curr[W]

print(knapsack01_4([8,2,5],[2,3,9], 8, 3))
print(knapsack01_4([2,2,5],[2,3,9], 9, 3))
print(knapsack01_4([2,2],[5,10], 3, 2))
print(knapsack01_4([1,2],[5,10], 3, 2))




