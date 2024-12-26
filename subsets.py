"""
Subsets or Power Set
Question:

Power Set - Given an integer array of unique elements, return all possible subsets (the power set). 
The solution set must not contain duplicate subsets. Return the solution in any order.
Example: [1,2,3]=[[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]  :: (2^n subsets from an array)
"""

def subsets(arr):
    n=len(arr)
    res=[]

    def helper(index, subset):
        
        if index==n:
            res.append(subset[:])
            return

        helper(index+1, subset)
        subset.append(arr[index])
        helper(index+1, subset)
        subset.pop()

    helper(0, subset=[])
    return res

print(subsets([1,2,3]))
print(subsets([1,1,2]))
print(len(subsets(['a','a','b','a'])))



"""
Coding Exercise: Subsets 2
Given an integer array nums that may contain duplicates, return all possible
subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example :
nums = [1,1,2]
Output =[[1, 1, 2], [1, 1], [1, 2], [1], [2], []]
"""

def subset2(arr):

    n=len(arr)
    res=[]

    def helper(index, subset):
        
        if index==n:
            res.append(subset[:])
            return
        
        #include
        subset.append(arr[index])
        helper(index+1, subset)
        subset.pop()

        #exclude
        while index<n-1 and arr[index]==arr[index+1]:
            index+=1

        helper(index+1, subset)

    helper(0, subset=[])
    return res

print(subset2([1,1,2]))
print(len(subset2(['a','a','b','a'])))

