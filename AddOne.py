# Given a list of digits representing a number, return a list with digits representing number+1

def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    number = ""
    newArr = []
    for a in arr:
        number = number + str(a)
    number = int(number) + 1
    newArr = [int(i) for i in list(str(number))]
    return newArr

print(add_one([9,9,9]))