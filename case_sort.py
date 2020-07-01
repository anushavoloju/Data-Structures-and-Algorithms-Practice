# sort the string retaining the case positions

def case_sort(string):
    """
    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output list
        else:
            pick upper-case character from sorted string to place in output list
    
    Note: You can use Python's inbuilt ord() function to find the ASCII value of a character
    """
    sorted_string = case_sort_mergesort(string)
    upperstring = ""
    lowerstring = ""
    for char in sorted_string:
        if char.islower():
            lowerstring = lowerstring + char
        if char.isupper():
            upperstring = upperstring + char
    final_sorted = ""
    upper_index = 0
    lower_index = 0
    for char in string:
        if char.islower():
            final_sorted = final_sorted + lowerstring[lower_index]
            lower_index = lower_index + 1
        if char.isupper():
            final_sorted = final_sorted + upperstring[upper_index]
            upper_index = upper_index + 1
    #print(sorted_string)
    #print(final_sorted)
    return final_sorted


def case_sort_mergesort(string):
    if len(string) <= 1:
        return string
    mid = len(string) // 2
    left = string[0:mid]
    right = string[mid:]
    left = case_sort_mergesort(left)
    right = case_sort_mergesort(right)
    return merge(left,right)

def merge(left,right):
    merged = ""
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged = merged + right[right_index]
            right_index += 1
        else:
            merged = merged + left[left_index]
            left_index += 1
    merged = merged + left[left_index:]
    merged = merged + right[right_index:]
    return merged



print(case_sort("fedRTSersUXJ"))