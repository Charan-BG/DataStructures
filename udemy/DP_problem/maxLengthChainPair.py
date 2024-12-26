"""
Coding Exercise: Max Length of Pair Chain
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.
"""

# TC=O(n*logn) (SC=(n) or #SC=O(1)
# def maxLength(nums):
#     n= len(nums)
#     nums.sort(key=lambda x:x[0])
#     # print(nums)
#     result=[nums[0]]
#     # maxlength=1

#     for start, end in nums[1:]:
#         last_end=result[-1][1]
#         if last_end<start:
#             result.append([start,end])
#             # maxlength+=1
#     print(result)
#     return len(result)
# 
# #this above method is not suitable since it gives suboptimal solution   

# TC=O(n^2) SC=O(n)
def MaxLength(pairs):
    n=len(pairs)
    pairs.sort()
    dp=[1]*(n)
    maxlength=1

    for i in range(1,n):
        for j in range(i):

            if pairs[j][1]<pairs[i][0] and dp[j]+1>dp[i]:
                dp[i]=dp[j]+1

        if dp[i]>maxlength:
            maxlength=dp[i]

    return maxlength


nums1=[[1,2], [7,9], [5,6], [3,4], [21,23], [1,8]]
nums=[[1,2], [5,9],[3,4],[5,6],[7,8],[9,10],[11,12]]
# print(maxLength(nums)) # 4 dont use this method since it gives suboptimal solution
# [[1, 2], [3, 4], [5, 9], [11, 12]]


print(MaxLength(nums)) # 6 so use this method LIS
# [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]