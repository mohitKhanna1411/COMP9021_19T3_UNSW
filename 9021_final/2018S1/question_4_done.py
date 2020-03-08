import sys
from math import sqrt
from itertools import compress


def f(n):
    '''
    Won't be tested for n greater than 10_000_000
    
    >>> f(3)
    The largest prime strictly smaller than 3 is 2.
    >>> f(10)
    The largest prime strictly smaller than 10 is 7.
    >>> f(20)
    The largest prime strictly smaller than 20 is 19.
    >>> f(210)
    The largest prime strictly smaller than 210 is 199.
    >>> f(1318)
    The largest prime strictly smaller than 1318 is 1307.
    '''
    if n <= 2:
        sys.exit()
    largest_prime_strictly_smaller_than_n = 0
    # Insert your code here
    list_prime = list()
    def prime_number(number):
        if number > 1:
            if number == 2:
                list_prime.append(number)
            if number > 2 and number % 2 == 0:
                return
            for d in range(3, int(sqrt(number)+ 1), 2):
                if number % d == 0:
                    return
            list_prime.append(number)
    for num in range(n):
        prime_number(num)
    largest_prime_strictly_smaller_than_n = sorted(list_prime)[-1]
    print(f'The largest prime strictly smaller than {n} is {largest_prime_strictly_smaller_than_n}.')
if __name__ == '__main__':
    import doctest
    doctest.testmod()
