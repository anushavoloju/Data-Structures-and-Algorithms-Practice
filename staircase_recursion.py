# return number of possible ways in which you can climb the staircase

"""
param: n - number of steps in the staircase
Return number of possible ways in which you can climb the staircase
"""
def staircase(n):
    '''Hint'''
    # Base Case - What holds true for minimum steps possible i.e., n == 0, 1, 2 or 3? Return the number of ways the child can climb n steps.
    
    # Recursive Step - Split the solution into base case if n > 3.
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return staircase(n-3) + staircase(n-2) + staircase(n-1)


print(staircase(5))