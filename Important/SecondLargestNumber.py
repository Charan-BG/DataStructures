def SecondLargestNumber(nums):

    first = second = float('-inf')

    for num in nums:
        if num>first:
            second=first
            first=num
        elif num>second:
            second=num

    return second

print(SecondLargestNumber([2,4,3,10,1,42,53,11,12,20]))

def ThirdLargestNumber(nums):

    first = second = third= float('-inf')

    for num in nums:
        if num>first:
            third=second
            second=first
            first=num
        elif num>second:
            third=second
            second=num
        else:
            third=num

    return third

print(ThirdLargestNumber([2,4,3,10,1,42,53,11,12,20]))