# return possible subsets of given list
def subsets(arr):
    """
    :param: arr - input integer array
    Return - list of lists (two dimensional array) where each list represents a subset
    TODO: complete this method to return subsets of an array
    """
    subsets_lists = []
    subsets_lists.append([])

    #print(arr)

    if len(arr) == 1:
        subsets_lists.append([arr[0]])
    else:
        first = arr[0]
        remaining = arr[1:]

        sub_subsets_list = subsets(remaining)

        for sub_sublist in sub_subsets_list:
            newlist = [first] + sub_sublist
            subsets_lists.append(newlist)
    return subsets_lists

#print(subsets([9, 12, 15]))


# Solution
def subsets_list(arr):
    return return_subsets(arr, 0)

def return_subsets(arr, index):
    if index >= len(arr):
        return [[]]

    small_output = return_subsets(arr, index + 1)

    #print(small_output)

    output = list()
    # append existing subsets
    for element in small_output:
        output.append(element)

    # add current elements to existing subsets and add them to the output
    for element in small_output:
        current = list()
        current.append(arr[index])
        current.extend(element)
        output.append(current)
    return output

print(subsets_list([9, 12, 15]))