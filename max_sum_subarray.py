# Given an input array, find the maximum sum of a contiguous subarry

def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    sum = arr[0]
    max_sum = arr[0]
    for i in range(1,len(arr)):
        sum = max(sum + arr[i], arr[i])
        max_sum = max(sum, max_sum)

    return max_sum

print(max_sum_subarray([1, 2, -5, -4, 1, 6]))