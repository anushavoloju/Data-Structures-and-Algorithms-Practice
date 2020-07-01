# find maximum subarray using recursion
'''
Pseudocode and Time Complexity Analysis
maxSubArrayRecursive(arr, start, stop)     T(n)
  1. if (start==stop):
      return arr[start]

  2. Calculate mid index       constant

  3. L = maxSubArrayRecursive(arr, start, mid)       T( 𝑛2 )

  4. R = maxSubArrayRecursive(arr, mid+1, stop)       T( 𝑛2 )

  5. C = maxCrossingSum(arr, start, mid, stop)         Θ(𝑛) 

  6. return max(C, max(L,R))       constant


Total time of execution  𝑇(𝑛)  =  2∗𝑇(𝑛2)+Θ(𝑛)≡𝑂(𝑛𝑙𝑜𝑔𝑛)
'''

def maxSubArray(arr):
    '''
    param: An array `arr`
    return: The maximum sum of the contiguous subarray. 
    No need to return the subarray itself.
    '''
    start = 0
    stop = len(arr)-1
    output = maxSubArrayRecursive(arr, start, stop)
    return output

def maxSubArrayRecursive(arr, start, stop):
    if start == stop:
        return arr[start]
    if start < stop:
        mid = (start + stop) // 2
        left = maxSubArrayRecursive(arr, start, mid)
        right = maxSubArrayRecursive(arr, mid+1, stop)
        crossing = maxCrossingSum(arr, start, mid, stop)
        return max(crossing, max(left,right))
    else:
        return arr[start]


def maxCrossingSum(arr, start, mid, stop):
    leftSum = arr[mid]
    leftMaxSum = arr[mid]

    for i in range(mid-1,start-1,-1):
        leftSum = leftSum + arr[i]
        if leftSum > leftMaxSum:
            leftMaxSum = leftSum

    rightSum = arr[mid+1]
    rightMaxSum = arr[mid+1]

    for j in range(mid+2,stop+1):
        rightSum = rightSum + arr[j]
        if rightSum > rightMaxSum:
            rightMaxSum = rightSum
    
    return leftMaxSum+rightMaxSum


print(maxSubArray([-2, 7, -6, 3, 1, -4, 5, 7]))