import sys
from math import sqrt

def get_all_proper_divisor(n):
    result = []
    for d in range(1,n):
        if n % d == 0:
            result.append(d)
    return result
def f(n):
    '''
    A number n is deficient if the sum of its proper divisors,
    1 included and itself excluded,
    is strictly smaller than n.
    
    >>> f(1)
    1 is deficient
    >>> f(2)
    2 is deficient
    >>> f(3)
    3 is deficient
    >>> f(6)
    6 is not deficient
    >>> f(29)
    29 is deficient
    >>> f(30)
    30 is not deficient
    >>> f(47)
    47 is deficient
    >>> f(48)
    48 is not deficient
    '''
    #input your code
    div_list = sorted(get_all_proper_divisor(n))
    # if n in div_list:

    #     del div_list[-1]
    if n == 1 or sum(div_list) < n:
        print(f'{n} is deficient')
    else:
        print(f'{n} is not deficient')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
