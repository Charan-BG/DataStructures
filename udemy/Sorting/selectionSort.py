#TC=O(n^2) in all case
#SC=O(1)

def selection(array):
    
    for i in range(len(array)):
        smallest=i
        for j in range(i+1, len(array)):

            if array[smallest]>array[j]:
                smallest=j

        if smallest!=i:
            array[i], array[smallest]=array[smallest], array[i]

    return array

array=[1,2,5,4,3]
array=[1,2,5,4,3,5,2,7,8,1,11,56,21,32,42,1]
print(selection(array))