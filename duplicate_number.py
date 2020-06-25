# Given and array containing numbers in the range [0, len(arr) - 2], return the number that is duplicate in the given array

def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    arr.sort()
    for i in range(len(arr)):
        if i == arr[i]:
            continue
        else:
            return arr[i]

print(duplicate_number([0, 2, 3, 1, 4, 5, 3]))