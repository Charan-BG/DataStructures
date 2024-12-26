# TC=O(logn)
# SC=O(1) for iteration if it is recursion SC=O(logn) due to call stack

def binary(nums, target):

    n=len(nums)
    left, right = 0, n-1

    while left<=right:
        mid = (left+right)//2

        if nums[mid]==target:
            return mid

        elif target<nums[mid]:
            right=mid-1

        else:
            left=mid+1

    return -1

nums=[2,4,6,7,8,9]
target=10
print(binary(nums, target)) 