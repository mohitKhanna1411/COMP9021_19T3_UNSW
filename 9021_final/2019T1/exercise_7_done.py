from itertools import combinations
# POSSIBLY DEFINE OTHER

def subnumbers_whose_digits_add_up_to(number, sum_of_digits):
    '''
    You can assume that "number" consists of digits not equal to 0
    and that "sum_of_digits" is an integer.

    A solution is obtained by possibly deleting some digits in "number"
    (keeping the order of the remaining digits) so that the sum of
    of the remaining digits is equal to "sum_of_digits".

    The solutions are listed from smallest to largest, with no duplicate.

    >>> subnumbers_whose_digits_add_up_to(13, 2)
    []
    >>> subnumbers_whose_digits_add_up_to(222, 2)
    [2]
    >>> subnumbers_whose_digits_add_up_to(123, 6)
    [123]
    >>> subnumbers_whose_digits_add_up_to(222, 4)
    [22]
    >>> subnumbers_whose_digits_add_up_to(1234, 5)
    [14, 23]
    >>> subnumbers_whose_digits_add_up_to(12341234, 4)
    [4, 13, 22, 31, 112, 121]
    >>> subnumbers_whose_digits_add_up_to(121212, 5)
    [122, 212, 221, 1112, 1121, 1211]
    >>> subnumbers_whose_digits_add_up_to(123454321, 10)
    [145, 154, 235, 244, 253, 343, 352, 442, 451, 532, 541, 1234, 1243, \
1252, 1342, 1351, 1432, 1441, 1531, 2332, 2341, 2431, 2521, 3421, \
4321, 12331, 12421, 13321]
    '''
    tempstr = list(str(number))

    comb_list = []
    
    for i in range(len(tempstr)+1):
        l = combinations(tempstr,i)
        for j in l:
            comb_list.append(j)

    f_comb_list = []

    for i in comb_list:
        t = ''.join(i)
        f_comb_list.append(t)

    #print(f_comb_list)

    sub_num_list = []

    for i in f_comb_list:
        tempsum = 0
        for j in i:
            tempsum = tempsum + int(j)
        if tempsum == sum_of_digits:
            sub_num_list.append(i)
        tempsum = 0

    f_sub_num_list = list(set(sub_num_list))

    fl = []

    for i in f_sub_num_list:
        j = int(i)
        fl.append(j)

    print(sorted(fl))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # subnumbers_whose_digits_add_up_to(123454321, 10)
    # print(subnumbers_whose_digits_add_up_to(123, 6))
    # print(sorted(subnumbers_whose_digits_add_up_to(123454321, 10)))
