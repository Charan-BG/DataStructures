#TC=O(n^2)in worst and average case, O(n) in best case
#SC=O(1)

def insertion(array):

    for i in range(1, len(array)):

        j=i-1
        temp=array[i]
        while j>=0 and array[j]>temp:
            array[j+1]=array[j]
            j-=1
        array[j+1]=temp

    return array

array=[1,2,5,4,3]

# i=4,j=3
# [1,2,4,5,3]

print(insertion(array))