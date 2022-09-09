
myarray = [3,2,1,7,9,10,32]

def ascend_sort(array):
    array.sort(reverse = False)
    return array


def descend_sort(array):
    array.sort(reverse = True)
    return array

# prints array in ascending order
print(ascend_sort(myarray))

# prints array in descending order
print(descend_sort(myarray))

