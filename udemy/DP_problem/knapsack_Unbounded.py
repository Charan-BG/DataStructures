def unboundedKnapsack(wt,val,W,N):

    dp=[[0]*(W+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, W+1):

            exclude=dp[i-1][j]
            include=0
            if wt[i-1]<=j:
                include=val[i-1]+dp[i][j-wt[i-1]]

            dp[i][j]=max(exclude, include)

    return dp[N][W]

print(unboundedKnapsack([2,2],[5,10],4,2))
#TC=O(n*w), SC=O(n*w)

#TC=O(n*w), SC=O(w)
def optimizedUnboundedKnapsack(wt,val,W,N):

    prev=[0]*(W+1)
    curr=[0]*(W+1)

    for i in range(1, N+1):
        for j in range(1, W+1):

            exclude=prev[j]
            include=0
            if wt[i-1]<=j:
                include=val[i-1]+curr[j-wt[i-1]]

            curr[j]=max(exclude, include)

    return curr[W]

print(optimizedUnboundedKnapsack([2,2],[5,10],4,2))
