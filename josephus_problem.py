"""
Question 2: Josephus problem: There are n friends that are playing a game. The friends are sitting in a circle and 
are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th
friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

1.Start at the 1st friend.

2.Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.

3.The last friend you counted leaves the circle and loses the game.

4.If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.

5.Else, the last friend in the circle wins the game.

Given the number of friends, n, and an integer k, return the winner of the game.
"""

# TC=O(n) SC=O(n)
def josephus(n, k):

    def helper(n):
        if n==1: return 0

        return (helper(n-1)+k) %n

    return helper(n) +1
    

print(josephus(4, 3))

# 1,2,3,4

# 3=3
# 3=2
# 3=4

# TC=O(n) SC=O(1)
def optimized_josephus(n, k):

    res=0
    for i in range(2, n+1):
        res = (res+k) %i

    return res+1
print(optimized_josephus(5, 3))


# 1,2,3,4,5

# res=1 ::2
# res=1 ::3
# res=0 ::4
# res=3 ::5


def fact(n):

    def helper(n):
        if n==1: return 1
        return n*helper(n-1)

    return helper(n)
    
print(fact(5))

def pattern(n):
    def helper(n):
        if n==0: return 0

        print(n)
        helper(n-1)
        print(n)

    return helper(n)
    
print(pattern(5))