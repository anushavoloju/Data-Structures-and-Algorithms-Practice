# return reverse of nested lists
def deep_reverse(arr):

    reverse_arr = []
    if len(arr) == 0:
        return []
    else:
        l = len(arr)-1
        while l >= 0:
            if type(arr[l]) == list:
                revlist = deep_reverse(arr[l])
                reverse_arr.append(revlist)
            else:
                reverse_arr.append(arr[l])
            l = l - 1
    return reverse_arr


print(deep_reverse([1, 2, [3, 4, 5], 4, 5]))