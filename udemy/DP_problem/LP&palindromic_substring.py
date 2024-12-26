"""
Palindromic Substrings
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "pqrp"
Output: 4
Explanation: Three palindromic strings: "p", "q", "r","p".
"""
#TC=O(n^2) for helper fun, SC=O(n^2)
def palindromicSubstring(s:str)->int:

    n=len(s)
    res=0
    dp=[[-1]*n for _ in range(n)]

    def helper(i,j):
        if i==j:
            dp[i][j]=True
            return dp[i][j]
        
        if dp[i][j]!=-1:
            return dp[i][j]
        
        helper(i,j-1)
        helper(i+1,j)
        if s[i]==s[j] and (j==i+1 or helper(i+1,j-1)):
            dp[i][j]=True
        else:
            dp[i][j]=False

    helper(0,n-1)

    for l in range(1,n+1):
        for i in range(0,n-l+1):
            j=i+l-1

            if dp[i][j]:
                res+=1

    return res

# print(palindromicSubstring("pqrp"))
# print(palindromicSubstring("a"))
# print(palindromicSubstring("abcd"))
# print(palindromicSubstring("aba"))
# print(palindromicSubstring("abaa"))
print(palindromicSubstring("pqestseqp"))


def palindromicSubstring2(s:str)->int:

    n=len(s)
    res=0
    dp=[[0]*n for _ in range(1,n+1)]
    
    for l in range(1,n+1):
        for i in range(n-l+1):
            j=i+l-1

            if i==j:
                dp[i][j]=True
                res+=1
            elif s[i]==s[j] and (j==i+1 or dp[i+1][j-1]):
                dp[i][j]=True
                res+=1
            else:
                dp[i][j]=False

    return res

print(palindromicSubstring2("abaa"))
print(palindromicSubstring2("pqestseqp"))



"""
Coding Exercise: Longest Palindromic Substring
Given a string s, return the longest  palindromic substring in s.

Example :
Input: s = "pabad"
Output: "aba"
"""

def LongestPalindromicSubstring(s:str)->str:

    n=len(s)
    res=s[0]

    dp=[[0]*n for _ in range(n)]

    for l in range(1,n+1):
        for i in range(0,n-l+1):
            j=i+l-1

            if i==j:
                dp[i][j]=True                
            elif s[i]==s[j] and (j==i+1 or dp[i+1][j-1]):
                dp[i][j]=True
            else:
                dp[i][j]=False

            if dp[i][j]:
                res=s[i:j+1]

    return res

print(LongestPalindromicSubstring("pabad"))