# List of permutations of the given list of elements using recursion

import copy

def permute(inputList):
    """
    Args: myList: list of items to be permuted
    Returns: list of permutation with each permuted item being represented by a list
    """

    permutationList = []

    if len(inputList) == 0:
        permutationList.append([])
        
    else:
        first = inputList[0]            
        remaining = inputList[1:]  

        sub_permutationList = permute(remaining)
        
        for permList in sub_permutationList:
            for l in range(0, len(permList) + 1): 
                newList = copy.deepcopy(permList)
                newList.insert(l, first)
                permutationList.append(newList)
                
    return permutationList
    


print(permute([0,1,2]))