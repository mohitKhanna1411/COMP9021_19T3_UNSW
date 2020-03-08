from itertools import compress,accumulate
from math import sqrt
import operator

def single_factors(number):
    '''
    Returns the product of the prime divisors of "number"
    (using each prime divisor only once).

    You can assume that "number" is an integer at least equal to 2.

    >>> single_factors(2)
    2
    >>> single_factors(4096)                 # 4096 == 2**12
    2
    >>> single_factors(85)                   # 85 == 5 * 17
    85
    >>> single_factors(10440125)             # 10440125 == 5**3 * 17**4
    85
    >>> single_factors(154)                  # 154 == 2 * 7 * 11
    154
    >>> single_factors(52399401037149926144) # 52399401037149926144 == 2**8 * 7**2 * 11**15
    154
    '''
    prime_list = list()
    while number % 2 == 0:
        prime_list.append(2)
        number = number // 2
    for d in range(3, int(sqrt(number))+1,2):
        while number % d == 0:
            prime_list.append(d)
            number = number // d
    if number > 2:
        prime_list.append(number)
    result = 1
    # print(prime_list)
    for i in set(prime_list):
        result = result * i
    print(result)
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
