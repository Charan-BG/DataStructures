"""
Coding Exercise: Tribonacci
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""
def triboncci(n):
    if n<=1: return n
    if n==2: return 1

    prev1=0
    prev2=1
    curr=1
    count=2
    while count<n:
        count+=1
        next=prev1+prev2+curr
        prev1=prev2
        prev2=curr
        curr=next

    return curr

print(triboncci(0))
print(triboncci(1))
print(triboncci(2))
print(triboncci(3))
print(triboncci(4))
print(triboncci(5))

