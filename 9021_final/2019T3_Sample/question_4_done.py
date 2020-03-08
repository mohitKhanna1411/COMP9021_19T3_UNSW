# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 4
 

'''
Will be tested with a at equal equal to 2 and b at most equal to 10_000_000.
'''
    

import sys
from math import sqrt, floor


def f(a, b):
    '''
    >>> f(2, 2)
    There is a unique prime number between 2 and 2.
    >>> f(2, 3)
    There are 2 prime numbers between 2 and 3.
    >>> f(2, 5)
    There are 3 prime numbers between 2 and 5.
    >>> f(4, 4)
    There is no prime number between 4 and 4.
    >>> f(14, 16)
    There is no prime number between 14 and 16.
    >>> f(3, 20)
    There are 7 prime numbers between 3 and 20.
    >>> f(100, 800)
    There are 114 prime numbers between 100 and 800.
    >>> f(123, 456789)
    There are 38194 prime numbers between 123 and 456789.
    '''
    number_of_primes_at_most_equal_to_b = 0
    # Insert your code here
    prime_list = list()
    def prime(n):
        if n > 1:
            if n == 2:
                prime_list.append(2)
            if n > 2 and n % 2 == 0:
                return
            for d in range(3, floor(sqrt(n) + 1), 2):
                if n % d == 0:
                    return
            if n > 2:
                prime_list.append(n)
    for n in range(a, b+1):
        prime(n)
    # print(prime_list)
    if not len(prime_list):
        print(f'There is no prime number between {a} and {b}.')
    elif len(prime_list) == 1:
        print(f'There is a unique prime number between {a} and {b}.')
    elif len(prime_list) > 1:
        print(f'There are {len(prime_list)} prime numbers between {a} and {b}.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # f(2, 3)
