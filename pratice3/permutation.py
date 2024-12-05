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

def permutation(arr):
    res=[]
    n=len(arr)

    def helper(index):
        if index == n:
            res.append(arr[:])
            return
        
        for i in range(index, n):

            arr[index], arr[i]=arr[i], arr[index]
            helper(index+1)
            arr[index], arr[i]=arr[i], arr[index]

    helper(0)

    return res


print(permutation([1,4,5]))


"""
Permutations 2
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example:

nums = [3,3,2]

Output :

[[3,3,2] , [3,2,3], [2,3,3] ]
"""

def permutation2(arr):
    res=[]
    n=len(0)

    def helper(index):

        if index==n:
            res.append(arr[:])
            return
        hash={}
        for i in range(index, n):

            hash[arr[i]]==



    helper(0)
    return res

