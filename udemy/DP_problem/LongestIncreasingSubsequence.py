
# Approach 1
# TC=O(2^n), SC=O(n)
def LIS(nums):

    n=len(nums)

    def helper(currIDX, prevIDX):
        
        if currIDX>n-1:
            return 0
        
        exclude= helper(currIDX+1, prevIDX)
        include= 0
        if nums[currIDX]>nums[prevIDX] or prevIDX==-1:
            include=1+helper(currIDX+1, currIDX)
        
        return max(exclude, include)

    return helper(0, -1)

# input = [1,2,3] #output= 3
# print(LIS(input))
# input = [3,2,1] #output= 1
# print(LIS(input))
# input = [1] #output= 1
# print(LIS(input))
input = [20,1,2,6,43,22,31,54] #output= 6
print(LIS(input))

# Approach 2
# TC=O(n^2), SC=O(n^2)
def LIS2(nums):

    n=len(nums)
    dp=[[-1]*n for _ in range(n)]

    def helper(currIDX, prevIDX):
        
        if currIDX>n-1:
            return 0
        if dp[currIDX][prevIDX+1]!=-1:
            return dp[currIDX][prevIDX+1]
        
        exclude= helper(currIDX+1, prevIDX)
        include= 0
        if nums[currIDX]>nums[prevIDX] or prevIDX==-1:
            include=1+helper(currIDX+1, currIDX)
        
        dp[currIDX][prevIDX+1]= max(exclude, include)
        return dp[currIDX][prevIDX+1]

    return helper(0, -1)

# input = [1,2,3] #output= 3
# print(LIS2(input))
# input = [3,2,1] #output= 1
# print(LIS2(input))
# input = [1] #output= 1
# print(LIS2(input))
input = [20,1,2,6,43,22,31,54] #output= 6
print(LIS2(input))

#Approach 3 Tabulation 2D
# TC=O(n^2), SC=O(n^2)
def LIS3(nums):
    n=len(nums)

    dp=[[0]*(n+1) for _ in range(n+1)]
    
    for i in range(n-1, -1, -1):
        for j in range(i, -1, -1):

            exclude= dp[i+1][j]
            include= 0
            if j-1==-1 or nums[i]>nums[j-1]:
                include= 1+dp[i+1][i+1]

            dp[i][j] = max(exclude, include)

    return dp[0][0]

input = [20,1,2,6,43,22,31,54] #output= 6
print(LIS3(input))

# Tabulation using 1D
# TC=O(n^2) SC=O(n)
def LIs4(nums):

    n=len(nums)
    dp=[1]*(n)
    max_val=1

    for i in range(1,n):
        for j in range(i):

            if nums[i]>nums[j] and dp[j]+1>dp[i]:
                dp[i]=dp[j]+1

        if dp[i]>max_val:
            max_val=dp[i]

    # max_val=max(dp)
    return max_val

print(LIs4(nums=[20,1,2,6,43,22,31,54]))

# TC=O(n*log(n)) SC=O(n)
def LIS_BinarySearch(nums):
    
    n=len(nums)
    def binarySearch(sub, num):
        left, right=0, len(sub)-1

        while left<right:
            mid=(left+right)//2

            if sub[mid]<num:
                left=mid+1
            else:
                right=mid
        return left

    sub=[nums[0]]
    for num in nums[1:]:
        if sub[-1]<num:
            sub.append(num)

        else:
            index=binarySearch(sub, num)
            sub[index]=num

    return len(sub)
print(LIS_BinarySearch(nums=[20,1,2,6,43,22,31,54]))
