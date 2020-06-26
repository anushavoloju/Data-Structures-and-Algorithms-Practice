# List of all permutations of the given input string using recursion

def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    permutationList = []

    if len(string) == 1:
        permutationList.append(string)
        
    else:
        first = string[0]          
        remaining = string[1:]   

        sub_permutationList = permutations(remaining)
        
        for sub_string in sub_permutationList:
            for l in range(0, len(sub_string) + 1): 
                newstring = str(sub_string[:l]) + str(first) + str(sub_string[l:])
                permutationList.append(newstring)
                
    return permutationList

print(permutations('abc'))