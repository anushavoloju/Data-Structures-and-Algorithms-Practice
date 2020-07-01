# return the last index of the target in the list
def last_index(arr, target):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    """
    if len(arr) == 0:
        return -1
    elif len(arr) == 1:
        if arr[0] == target:
            return 0
        else:
            return -1
    else:
        if target in arr:
            temp_index = arr.index(target)
            #prefix = arr[0:temp_index+1]
            remaining = arr[temp_index+1:]
            index = temp_index + last_index(remaining, target) + 1
            if index == -1:
                return temp_index
            else:
                return index
        else:
            return -1

print(last_index([1, 1, 1, 1, 1, 1], 1))