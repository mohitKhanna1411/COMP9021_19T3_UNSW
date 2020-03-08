
def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.
    
    
    >>> is_heterosquare([[1, 2, 3],\
                         [8, 9, 4],\
                         [7, 6, 5]])
    True
    >>> is_heterosquare([[1, 2, 3],\
                         [9, 8, 4],\
                         [7, 6, 5]])
    False
    >>> is_heterosquare([[2, 1, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    True
    >>> is_heterosquare([[1, 2, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    False
    '''
    n = len(square)
    if any(len(line) != n for line in square):
        return False
    row_sum = 0
    col_sum = 0
    diag_sum_1 = 0
    diag_sum_2 = 0
    sum_list = list()
    # Insert your code here
    for i in range(n):
        for j in range(n):
            row_sum += square[i][j]
            col_sum += square[j][i]
            if i == j:
                diag_sum_1 += square[i][j]
        diag_sum_2 += square[i][n-i-1]
        # print(row_sum, col_sum)
        if row_sum in sum_list:
            return False
        else:
            sum_list.append(row_sum)
        if col_sum in sum_list:
            return False
        else:
            sum_list.append(col_sum)
        row_sum = 0
        col_sum = 0
    # print(diag_sum_1, diag_sum_2)
    if diag_sum_1 in sum_list:
        return False
    else:
        sum_list.append(diag_sum_1)
    if diag_sum_2 in sum_list:
        return False
    return True
# Possibly define other functions

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
