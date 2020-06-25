# Implement Pascals Triangle

def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    if n == 0:
        return [1]
    if n == 1:
        return [1,1]
    row = 2
    while row <= n:
        previous_row = nth_row_pascal(row-1)
        nth_row = []
        nth_row.append(1)
        for i in range(1,len(previous_row)):
            nth_row.append(previous_row[i] + previous_row[i-1])
        nth_row.append(1)
        row = row + 1
    return nth_row

print(nth_row_pascal(1))