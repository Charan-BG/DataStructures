"""
Coding Exercise: Partition Equal Subset Sum
Given an integer array nums, return true if you can partition the array into two subsets such 
that the sum of the elements in both subsets is equal or false otherwise.
Example 1:

Input: nums = [1,5,20,14]
Output: true
Explanation: The array can be partitioned as [1, 5, 14] and [20].
"""

def partitionSum(nums):
    n=len(nums)
    total_sum=sum(nums)
    
    if total_sum%2 !=0:
        return False
    
    target=total_sum//2
    
    dp=[[True]*(target+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, target+1):
            #pick
            if nums[i-1]<=j:
                dp[i][j] = dp[i-1][j-nums[i-1]]
            else:
                dp[i][j] = False
            #dont pick
            dp[i][j]=dp[i-1][j] or dp[i][j]

    return dp[n][target]

print(partitionSum([1,1,2]))
print(partitionSum([1,1,3]))
print(partitionSum([1,1,2,1,1]))

def canPartition(nums):
    #Write code here
    n= len(nums)
    summ= sum(nums)
    
    if summ%2 !=0: return False
    
    target=summ//2
    prev=[True]*(target+1)
    curr=[True]*(target+1)
    prev[0]=True
    curr[0]=True
    
    for i in range(1, n+1):
        for j in range(1, target+1):
            #pick
            if nums[i-1]<=j:
                curr[j]=prev[j-nums[i-1]]
            else:
                curr[j] = False
            #dont pick
            curr[j]=curr[j] or prev[j]
            
        prev=curr[:]
    return curr[target]

print(canPartition([1,1,2]))