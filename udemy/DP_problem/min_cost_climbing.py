"""
Coding Exercise: Minimum Cost Climbing Stairs
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, 
you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,20,30]
Output: 20

Explanation: You will start at index 1.
- Pay 20 and climb two steps
"""
import time
#Approach 1 TC=O(2^n), SC=O(n)
start_time=time.time()
def min_cost_climb(cost):
    n=len(cost)
    

    def helper(index):
        
        #base case
        if index>n-1:
            return 0
        
        #recursive case
        onestep= cost[index]+helper(index+1)

        twostep= cost[index]+helper(index+2)

        return min(onestep, twostep)
    return min(helper(0), helper(1))



# print(min_cost_climb([1,2,3])) #2
# print(min_cost_climb([10,20,30])) #20
print(min_cost_climb([10, 15, 20, 5, 15, 25, 30, 10, 5, 20, 10, 15, 25, 30, 5, 20, 30, 10, 5, 20, 10, 25, 15, 30, 10, 5, 15, 20, 30, 10]))
end_time=time.time()
print(end_time-start_time)

#Approach 2 TC=O(n) coz we compute the tree once and store it in mincost array, SC=O(n) call stack
start_time=time.time()
def min_cost_climb2(cost):
    n=len(cost)
    mincost=[-1]*n

    def helper(index):
        
        #base case
        if index>n-1:
            return 0
        
        #recursive case
        if mincost[index]!=-1:
            return mincost[index]
        onestep= cost[index]+helper(index+1)

        twostep= cost[index]+helper(index+2)
        mincost[index] = min(onestep, twostep)

        return mincost[index]
    return min(helper(0), helper(1))



# print(min_cost_climb2([1,2,3]))
# print(min_cost_climb2([10,20,30]))
print(min_cost_climb2([10, 15, 20, 5, 15, 25, 30, 10, 5, 20, 10, 15, 25, 30, 5, 20, 30, 10, 5, 20, 10, 25, 15, 30, 10, 5, 15, 20, 30, 10]))
end_time=time.time()
print(end_time-start_time)

#Tabulation
#Approach 3 TC=O(n) for 2,n+1 iter, SC=O(n) for mincost array
start_time=time.time()
def min_cost_climb3(cost):
    n=len(cost)
    mincost=[0]*(n+1)
    mincost[0]=0
    mincost[1]=0

    for i in range(2, n+1):
            
        onestep = cost[i-1]+mincost[i-1]
        twostep = cost[i-2]+mincost[i-2]

        mincost[i]=min(onestep, twostep)
    
    return mincost[n]

# 0,1,2, 3(n+1)   cost=[1,2,3]
# 0,0,1, min(2,3)

# onestep|cost[i-1]+mincost[i-1]
# twostep|cost[i-2]+mincost[i-2]

# cal min(onestep,twostep)
print(min_cost_climb3([1,2,3]))
print(min_cost_climb3([10,20,30]))
print(min_cost_climb3([10, 15, 20, 5, 15, 25, 30, 10, 5, 20, 10, 15, 25, 30, 5, 20, 30, 10, 5, 20, 10, 25, 15, 30, 10, 5, 15, 20, 30, 10]))
end_time=time.time()
print(end_time-start_time)



