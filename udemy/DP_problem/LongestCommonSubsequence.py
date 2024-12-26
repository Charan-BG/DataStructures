"""
Coding Exercise: LCS ( Longest Common Subsequence)
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

•For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example: 

Input: text1 = "pbcdq", text2 = "pcq" 
Output: 3  
Explanation: The longest common subsequence is "pcq" and its length is 3.
"""
# TC=O(2^n+m), SC=O(n+m)
def LCS(text1, text2):
    n=len(text1)
    m=len(text2)

    def helper(i, j):

        if i>n-1 or j>m-1:
            return 0
        
        if text1[i] == text2[j]:
            return 1+helper(i+1, j+1)
        else:
            return max(helper(i+1, j), helper(i, j+1))


    return helper(0,0)

print(LCS('abcde', 'abe'))
print(LCS('abcde', 'abec'))
print(LCS('abcde', 'abce'))
print(LCS('a', 'a'))
print(LCS(' ', 'a'))

#Approach 2
# TC=O(n*m), SC=O(n*m) : O(n*m)+O(n+m) [table, call stack] 
def LCS2(text1, text2):
    n=len(text1)
    m=len(text2)

    dp=[[-1]*m for _ in range(n)]
    def helper(i, j):

        if i>n-1 or j>m-1:
            return 0

        if dp[i][j] !=-1:
            return dp[i][j]

        if text1[i] == text2[j]:
            dp[i][j]= 1+helper(i+1, j+1)
        else:
            dp[i][j]= max(helper(i+1, j), helper(i, j+1))

        return dp[i][j]

    return helper(0,0)

print(LCS2('abcde', 'abe'))
print(LCS2('abcde', 'abec'))
print(LCS2('abcde', 'abce'))
print(LCS2('a', 'a'))
print(LCS2(' ', 'a'))

# abcde
# abe

# # n=5, m=3, i=0, j=0, a==a, 1+(i+1)(j+1)                   << 1+(1)+(1)
# # n=5, m=3, i=1, j=1, b==b, 1+1+(i+2)(j+2)                 << 1+(1)
# # n=5, m=3, i=2, j=2, c==e, max((i+1, j)(i, j+1))          << 1 
# #     (i+1, j) :: n=5, m=3, i=3, j=2, d==e, max((i+1, j)(i, j+1))
# #         (i+1, j) :: n=5, m=3, i=4, j=2, e==e, 1+(i+1, j+1) >> i=5,j=2 return 0
# #     (i, j+1) :: n=5, m=3, i=2, j=3, return 0
# # max((i+1, j)(i, j+1)) >> return max(1,0)

# TC=O(n*m) [for dp table], SC=O(n*m) [for i and j iteration]
def LCS3(text1, text2):

    n=len(text1)
    m=len(text2)

    dp=[[0]*(m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1, m+1):

            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]

print(LCS3('abcde', 'abe'))
print(LCS3('abcde', 'abec'))
print(LCS3('abcde', 'abce'))


# TC=O(n*m) [for dp table], SC=O(1)
def LCS3(text1, text2):

    n=len(text1)
    m=len(text2)

    # dp=[[0]*(m+1) for _ in range(n+1)]
    prev=[0]*(m+1)
    curr=[0]*(m+1)
    for i in range(1,n+1):
        for j in range(1, m+1):

            if text1[i-1] == text2[j-1]:
                curr[j] = prev[j-1]+1
            else:
                curr[j]= max(prev[j], curr[j-1])
        prev=curr[:]
    return curr[m]

print(LCS3('abcde', 'abe'))
print(LCS3('abcde', 'abec'))
print(LCS3('abcde', 'abce'))