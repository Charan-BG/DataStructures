"""
Coding Exercise: Search for range
Question:

Find First and Last Position of Element in Sorted Array-You are given an array of integers sorted 
in non-decreasing order, find the starting and ending position of a given target value. If target is 
not found in the array, return [-1, -1]. You must write an algorithm with O(log n) runtime complexity.

Try: Try to write both the iterative solution and recursive solution
"""
#TC=O(logn) since we are running two time binary search TC=O(2logn)
#SC=O(1) since we have used iteration

def search_for_range(array,target):
    #write your code here   
   
    def left_ext(array, target):
        n=len(array)
        left, right= 0, len(array)
        while left<=right:
        
            mid=(left+right)//2
            
            if array[mid]==target:
                if mid==0 or array[mid-1]!=target:
                    return mid
                        
                elif array[mid-1]==target:
                    right=mid-1

            elif target<array[mid]:
                right = mid-1
            else:
                left = mid+1
   
        return -1 
        
    def right_ext(array, target):
        n=len(array)
        left, right= 0, len(array)
       
        while left<=right:
            
            mid=(left+right)//2
            
            if array[mid]==target:
                if mid==n-1 or array[mid+1]!=target:
                    return mid
            
                elif array[mid+1]==target:
                    left=mid+1

            elif target<array[mid]:
                right = mid-1
            else:
                left = mid+1
              
        return -1
    
    ans_left = left_ext(array, target)
    ans_right = right_ext(array, target)
    return [ans_left, ans_right]


array=[1,1,1,3,4,7,7,7,7,8,9]
target=9
print(search_for_range(array, target))
            
            
        
        
