# find kth largest element in a list 
'''
The Pseudocode - fastSelect(Arr, k)

Break Arr into  𝑛5  (actually it is  ⌈𝑛5⌉ ) groups, namely  𝐺1,𝐺2,𝐺3...𝐺𝑛5 

For each group  𝐺𝑖,∀1≤𝑖≤𝑛5 , do the following:
Sort the group  𝐺𝑖 

Find the middle position i.e., median  𝑚𝑖  of group  𝐺𝑖 
Add  𝑚𝑖  to the set of medians  𝑆 

The set of medians  𝑆  will become as  𝑆={𝑚1,𝑚2,𝑚3...𝑚𝑛5} . 
The "good" pivot element will be the median of the set  𝑆 . We can find it as  𝑝𝑖𝑣𝑜𝑡=𝑓𝑎𝑠𝑡𝑆𝑒𝑙𝑒𝑐𝑡(𝑆,𝑛10) .

Partition the original Arr into three sub-arrays 
- Arr_Less_P, Arr_Equal_P, and Arr_More_P having elements less than pivot, equal to pivot, and bigger than pivot respectively.

Recurse based on the sizes of the three sub-arrays, 
we will either recursively search in the small set, or the big set, as defined in the following conditions:

If k <= length(Arr_Less_P), 
then return fastSelect(Arr_Less_P, k). 
This means that if the size of the "small" sub-array is at least as large as k, then we know that our desired  𝑘𝑡ℎ  smallest element lies in this sub-array. Therefore recursively call the same function on the "small" sub-array.


If k > (length(Arr_Less_P) + length(Arr_Equal_P)), 
then return fastSelect(Arr_More_P, (k - length(Arr_Less_P) - length(Arr_Equal_P))). 
This means that if k is more than the size of "small" and "equal" sub-arrays, then our desired  𝑘𝑡ℎ  smallest element lies in "bigger" sub-array.


Return pivot otherwise. 
This means that if the above two cases do not hold true, then we know that  𝑘𝑡ℎ  smallest element lies in the "equal" sub-array.
'''

def fastSelect(Arr, k):
    '''TO DO'''
    # Implement the algorithm explained above to find the k^th lasrgest element in the given array
    if len(Arr) < 1:
        return None
    if len(Arr) == 1:
        return Arr[0]
    
    groups = []
    index = 0
    while index < len(Arr):
        groups.append(Arr[index:index+5])
        index = index + 5
    #print(groups)

    medians = set()
    for index,group in enumerate(groups):
        groups[index] = sorted(group)
        mid = len(group) // 2
        medians.add(groups[index][mid])
    #print(groups, medians)
    pivot = fastSelect(list(medians), int(len(Arr)/10))

    Arr_Less_P = []
    Arr_Equal_P = []
    Arr_More_P = []
    for item in Arr:
        if item < pivot:
            Arr_Less_P.append(item)
        elif item > pivot:
            Arr_More_P.append(item)
        else:
            Arr_Equal_P.append(item)
    
    if k <= len(Arr_Less_P):
        return fastSelect(Arr_Less_P, k)
    elif k > len(Arr_Less_P) + len(Arr_Equal_P):
        return fastSelect(Arr_More_P, k - len(Arr_Less_P) - len(Arr_Equal_P))
    else:
        return pivot


print(fastSelect([6, 80, 36, 8, 23, 7, 10, 12, 42, 99], 5))