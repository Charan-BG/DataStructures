"""
Coding Exercise: Power Sum
Question:
Power Sum - Let’s define a peculiar type of array in which each element is either an integer or another peculiar array. 
Assume that a peculiar array is never empty. Write a function that will take a peculiar array as its input and find the 
sum of its elements. If an array is an element in the peculiar array you have to convert it to it’s equivalent value so 
that you can sum it with the other elements. Equivalent value of an array is the sum of its elements raised to the number 
which represents how far nested it is. For e.g. [2,3,[4,1,2]] = 2+3+ (4+1+2)^2

another example - [1,2,[7,[3,4],2]] = 1 + 2 +( 7+(3+4)^3+2)^2
"""
# TC-O(N), SC-O(d)
# N-total number of elements in a list also consider list ele to :: d-highest power depth [1, [[2]]] d=3 
def power_sum(arr):
    pow=1
    
    def helper(arr, pow):
        # nonlocal sum
        sum=0
        for i in arr:
            if type(i)==list:
                sum+=helper(i, pow+1)
                # print(sum)
            else:
                sum+=i
                # print(sum)
        return sum**pow

    return helper(arr, pow)

print(power_sum([2,3,[4,1,2,5], 10, 20]))


# def power_sum(arr, pow=1):
#     # pow=1
#     sum=0
#     # def helper(arr, pow):
#     #     nonlocal sum
#     for i in arr:
#         if type(i)==list:
#             sum+=power_sum(i, pow+1)
#             print(sum)
#         else:
#             sum+=i
#             print(sum)
#     return sum**pow



# print(power_sum([2,3,[4,1,2]]))