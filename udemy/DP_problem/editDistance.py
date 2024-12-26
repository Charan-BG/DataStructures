"""
Coding Exercise: Edit Distance
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

•Insert a character

•Delete a character

•Replace a character

Example: 
Input: word1 = "hodse", word2 = "dos"
Output: 3
Explanation: 
hodse -> dodse (replace 'h' with 'd')
dodse -> dose (remove 'd')
dose -> dos (remove 'e')
"""
# Approach 1
# TC=O(3^n+m), SC=O(n+m)
def editDistance(word1, word2):

    n=len(word1)
    m=len(word2)

    def helper(i, j):

        if i>n-1 and j>m-1:
            return 0
        if i>n-1:
            return m-j
        
        if j>m-1:
            return n-i
        

        if word1[i]==word2[j]:
            return helper(i+1, j+1)
        insert=1+helper(i,j+1)
        delete=1+helper(i+1,j)
        replace=1+helper(i+1, j+1)

        return min(insert, delete, replace)
    
    return helper(0,0)

print(editDistance('abcde', 'ace'))
# print(editDistance('a', 'a'))
# print(editDistance(' ', 'a'))
# print(editDistance(' a', 'abcde'))


# Approach 2 # TC=O(n*m), SC=O(n*m) : O(n*m)+O(n+m) [table, call stack] 

def editDistance_2(word1, word2):

    n=len(word1)
    m=len(word2)

    dp=[[-1]*m for _ in range(n)]

    def helper(i, j):

        if i>n-1 and j>m-1:
            return 0
        if i>n-1:
            return m-j   
        if j>m-1:
            return n-i
        
        if dp[i][j]!=-1:
            return dp[i][j]

        if word1[i]==word2[j]:
            dp[i][j]= helper(i+1, j+1)
        else:
            insert=1+helper(i,j+1)
            delete=1+helper(i+1,j)
            replace=1+helper(i+1, j+1)

            dp[i][j]= min(insert, delete, replace)
        return dp[i][j]
    
    return helper(0,0)

# print(editDistance_2('abcde', 'ace'))
# print(editDistance_2('abc', 'ab'))
# print(editDistance_2('a', 'a'))
# print(editDistance_2(' ', 'a'))
# print(editDistance_2(' a', 'abcde'))

# Approach 3 TC=O(n*m), SC=O(n*m)
def editDistance_3(word1, word2):

    n=len(word1)
    m=len(word2)

    dp=[[0]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0]=i
    for j in range(m+1):
        dp[0][j]=j

    for i in range(n+1):
        for j in range(m+1):

            if word1[i-1] == word2[j-1]:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                               #insert     #delete     #replace
    return dp[n][m]


print(editDistance_3('abcde', 'ace')) 
# print(editDistance_2('abc', 'ab'))
# print(editDistance_2("kitten", "sitting"))


#    ' ' a b 
# ' '0   1 2
# a  1   0 (0+1)
# b  2   (1) 0
# c  3   (2) (1)

# =1

# Approach 4 TC=O(n*m), SC=O(m)
def editDistance_4(word1, word2):
    n=len(word1)
    m=len(word2)

    prev=[0]*(m+1)
    curr=[0]*(m+1)

    prev[1]=1

    for i in range(1,n+1):
        curr[0]=i
        for j in range(1,m+1):

            if word1[i-1]==word2[j-1]:
                curr[j]=prev[j-1]
            else:
                curr[j]=min(prev[j], curr[j-1], prev[j-1])+1

        prev=curr[:]

    return prev[m]

print(editDistance_4('abcde', 'ace')) 


