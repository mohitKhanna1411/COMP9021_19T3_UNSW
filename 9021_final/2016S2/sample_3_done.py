import sys
from math import sqrt

def f(a, b):
    '''
    The prime numbers between 2 and 12 (both included) are: 2, 3, 5, 7, 11
    The gaps between successive primes are: 0, 1, 1, 3.
    Hence the maximum gap is 3.
    
    Won't be tested for b greater than 10_000_000
    
    >>> f(3, 3)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 4)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 5)
    The maximum gap between successive prime numbers in that interval is 1
    >>> f(2, 12)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(5, 23)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(20, 106)
    The maximum gap between successive prime numbers in that interval is 7
    >>> f(31, 291)
    The maximum gap between successive prime numbers in that interval is 13
    '''
    if a <= 0 or b < a:
        sys.exit()
    max_gap = 0
    # Insert your code here
    prime_list =[]
    gap_list = []

    def prime_number(n):
        if n > 1:
            if n == 2:
                prime_list.append(n)
            if n > 2 and n % 2 == 0:
                return
            for d in range(3, int(sqrt(n) + 1),2):
                if n % d == 0:
                    return
            prime_list.append(n)
    
    for num in range(a,b+1):
        prime_number(num)
    max_gap = 0
    if len(prime_list) > 1:
        first = prime_list[0]
        for second in prime_list[1:]:
            gap_list.append(abs(second-first) - 1)
            first = second
        max_gap = max(gap_list)
    print(f'The maximum gap between successive prime numbers in that interval is {max_gap}')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
