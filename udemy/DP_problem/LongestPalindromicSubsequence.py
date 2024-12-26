"""
Coding Exercise: Longest Palindromic Subsequence
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements 
without changing the order of the remaining elements.

Example :
Input: s = "cccacpc"
Output: 5
Explanation: One possible longest palindromic subsequence is "ccccc".
"""

# TC=O(n^2) for find all the substrings, SC=O(n^2)
def LPS(s:str)->int:

    n=len(s)

    dp=[[0]*n for _ in range(n)]

    for l in range(1,n+1):
        for i in range(0,n-l+1):
            j=i+l-1

            if i==j:
                dp[i][j]=1
            elif s[i]==s[j]:
                dp[i][j]=2+dp[i+1][j-1]
            else:
                dp[i][j]=max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

print(LPS("cccacpc"))