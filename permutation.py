"""
Coding Exercise ( Permutations)
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
nums = [1,4]
Output :[[1,4],[4,1]]

Example 2:
nums = [1,4,5]
Output :[[1,4,5],[1,5,4],[4,1,5],[4,5,1],[5,1,4],[5,4,1]]
"""
# TC-O(n!*n) SC-O(n) (if we consider res space SC=O(n!*n))
def permutation(arr):

    n=len(arr)
    res=[]

    def helper(index):
        
        if index==n-1: 
            res.append(arr[:])
            return
        
        for j in range(index, n):
            arr[index], arr[j] = arr[j], arr[index]
            helper(index+1)
            arr[index], arr[j] = arr[j], arr[index]

    helper(0)
    return res

print(permutation([1,4,5]))
print(permutation([3,3,2]))
# print((10*9*8*7*6*5*4*3*2*1)*10)

"""
Permutations 2
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example:

nums = [3,3,2]

Output :

[[3,3,2] , [3,2,3], [2,3,3] ]
"""

def permutation2(arr):
    n=len(arr)
    res=[]

    def helper(index):
        
        if index==n-1: 
            res.append(arr[:])
            return
        
        hash={}
        for j in range(index, n):
            if arr[j] not in hash:
                hash[arr[j]] = True
            
                arr[index], arr[j] = arr[j], arr[index]
                helper(index+1)
                arr[index], arr[j] = arr[j], arr[index]


    helper(0)
    return res

print(permutation2([3,3,2]))

