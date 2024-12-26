"""
[1,2,3,4,5] = sorted

[1,2,8,5,7],
# 1stcycle
[1,2,8,5,7]
[1,2,8,5,7]
[1,2,5,8,7]
[1,2,5,7,8]  sorted=True 
"""
#TC=O(n^2) in worst ,TC=O(n) in bestcase
#SC=O(1)

def bubblesort(array):

    sorted=False
    counter=0

    while not sorted:
        sorted=True
        for i in range(len(array)-1-counter):
            if array[i]>array[i+1]:
                array[i],array[i+1] = array[i+1], array[i]
                sorted=False

        counter+=1

    return array

print(bubblesort([1,2,7,8,3]))