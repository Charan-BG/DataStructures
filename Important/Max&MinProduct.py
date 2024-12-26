def MaxProduct(nums):
    # nums.sort() #O(n*logn)
    # return max((nums[0]*nums[1]), (nums[-1]*nums[-2]))

    #or
    #O(n)
    firstP = secondP = float('-inf')
    firstN = secondN = float('+inf')
    for num in nums:
        if num>firstP:
            secondP=firstP
            firstP=num
        elif num>secondP:
            secondP=num

        if num<firstN:
            secondN=firstN
            firstN=num
        elif num<secondN:
            secondN=num

    return max((firstP*secondP), (firstN*secondN))


print(MaxProduct([1,4,5])) #20
print(MaxProduct([1,34,2,-10,-20,5])) #200


def _2ndMaxProduct(nums):
    # nums.sort()
    # return min((nums[0]*nums[1]), (nums[-1]*nums[-2]))

    #or
    #O(n)
    firstP = secondP = float('-inf')
    firstN = secondN = float('+inf')
    for num in nums:
        if num>firstP:
            secondP=firstP
            firstP=num
        elif num>secondP:
            secondP=num

        if num<firstN:
            secondN=firstN
            firstN=num
        elif num<secondN:
            secondN=num

    return min((firstP*secondP), (firstN*secondN))

print(_2ndMaxProduct([1,4,5])) #4
print(_2ndMaxProduct([1,34,2,-10,-20,5])) #170