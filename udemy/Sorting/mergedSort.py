#TC=O(nlogn) where n is the ele in each level and logn is the number of levels
# SC=O(n) where n is the array used to store final merged array. while recurion call stack holds function
#           therefore that whole ST=O(logn + n) since n>logn we say (O(n))

def merged(nums):

    def sort_array(array1, array2):
        i,j=0,0
        merged=[]

        while i<len(array1) and j<len(array2):
            if array1[i]<=array2[j]:
                merged.append(array1[i])
                i+=1
            else:
                merged.append(array2[j])
                j+=1

        while i<len(array1):
            merged.append(array1[i])
            i+=1
        while j<len(array2):
            merged.append(array2[j])
            j+=1

        return merged 

    def divide_array(nums):

        if len(nums)==1:
            return nums

        mid = len(nums)//2
        left_side= divide_array(nums[:mid])
        # print(left_side)
        right_side=divide_array(nums[mid:])
        # print()
        # print(right_side)

        return sort_array(left_side, right_side)
    
    return divide_array(nums)

array=[1,2,5,4,3]
# array=[1,2,5,4,3,5,2,7,8,1,11,56,21,32,42,1]
print(merged(array))