"""
# Coding Exercise: Combinations
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
Example:
n = 4
k=2
Output =[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
"""
# TC-O(n^C_r * n), SC-O(n)
#T-C = O(K*nCk)*O(1),   n=len(arr) and c=combinations and k=length which you need in result arr
#S-C = O(n) Recursive Call stack, remember space of the result arr is not calulated.
def combination(n, k):  #n=value, k=length of Carr
    res=[]

    def helper(start, curr):
        
        if len(curr)==k:
            res.append(curr[:])
            return
        
        need=k-len(curr)

        # for i in range(start, n+1)
        for i in range(start, n-need+2):
            curr.append(i)
            helper(i+1, curr)
            curr.pop()

    helper(1, [])
    return res

print(combination(4, 2))


"""
# Combinations Sum 1
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations 
of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency 
of at least one of the chosen numbers is different.

(the integers in the candidates array are all non negative )

Example 1:
Input: candidates = [2,3,8,9], target = 9
Output: [[2,2,2,3],[3,3,3],[9]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 2+ 3 = 9. Note that 2 can be used multiple times.
3 is a candidate and 3+3+3 = 9.
9 is a candidate, and 9 = 9.
These are the only two combinations.
"""

#T-C = O(N^(T/M+1)), where N=number of candidates, T=Target and M=minimum value among candidates
#S-C = O(T/M)
def com_sum(arr, target):
    n=len(arr)
    res=[]

    def helper(start, curr):
        
        if sum(curr)>target:
            return
        if sum(curr)==target:
            res.append(curr[:])
            return

        for i in range(start, n):

            curr.append(arr[i])
            helper(i, curr)
            curr.pop()

    helper(0, [])
    return res

print(com_sum([2,3,8,9], 9))


"""
# Coding Exercise: Combinations Sum 2
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates 
where the candidate numbers sum to target.Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
Example :
Input: candidates = [3,5,2,1,3], target = 7
Output: [[1,3,3],[5,2]]
"""
#T-C= O(2^n) where n =no. of nums value, each value can have 2 choose either INCLUDE or EXCLUDE
#s-c= O(n)
def com_sum2(arr, target):
    n=len(arr)
    res=[]
    arr.sort()
    
    def helper(start, curr):
        
        if sum(curr)==target:
            res.append(curr[:])
            return
        if sum(curr)>target:
            return
        if start>n-1:  #works without it but not sometime
            return
        
        hash={}
        for i in range(start, n):
            if arr[i] not in hash:
                hash[arr[i]]=True

                curr.append(arr[i])
                helper(i+1, curr)
                curr.pop()

    helper(0, [])
    return res

print(com_sum2([3,5,2,1,3], 7))


"""
# Coding Exercise: Combinations Sum 3
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and 
the combinations may be returned in any order.

Example :
Input: k = 6, n = 3
Output: [[1,2,3]] 
Explanation: 1 + 2 + 3 = 6
There are no other valid combinations.
"""
#T-C= O(K*nCk)
#S-C = O(n)
def comb_sum3(n, k): #n=length limit for an combination arr, k=target value when summed the Carr
    res=[]

    def helper(start, curr):

        if sum(curr)==k and len(curr)==n:
            res.append(curr[:])
            return
        if sum(curr)>k or len(curr)>n:
            return

        for i in range(start, 10):
            curr.append(i)
            helper(i+1, curr)
            curr.pop()


    helper(1, [])
    return res

print(comb_sum3(3, 6))

