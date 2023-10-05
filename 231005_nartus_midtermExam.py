'''
def maxFinderFunction(array)
    max element = initialized 2d array
        for row in 2darray
            for every element in array
                if said element > initialized array
                    do max element = said element 
    return max element

2DArray = [[0,0,0], [0,0,0], [0,0,0]]
result = maxFinderFunction(2DArray)
printf "the element is" + result     
'''
def maxFunc(array):
    max_element = array[0][0]
    for row in array:
        for element in row:
            if element > max_element:
                max_element = element
    return max_element

array2d = [
    [11,22,33],
    [44,55,66], 
    [77,88,99]]

result = maxFunc(array2d)
print(f"The largest element is:" , result)