# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 3


'''
Will be tested with n at least equal to 2, and "not too large".
'''
from math import *



def f(n):
    '''
    >>> f(2)
    The decomposition of 2 into prime factors reads:
       2 = 2
    >>> f(3)
    The decomposition of 3 into prime factors reads:
       3 = 3
    >>> f(4)
    The decomposition of 4 into prime factors reads:
       4 = 2^2
    >>> f(5)
    The decomposition of 5 into prime factors reads:
       5 = 5
    >>> f(6)
    The decomposition of 6 into prime factors reads:
       6 = 2 x 3
    >>> f(8)
    The decomposition of 8 into prime factors reads:
       8 = 2^3
    >>> f(10)
    The decomposition of 10 into prime factors reads:
       10 = 2 x 5
    >>> f(15)
    The decomposition of 15 into prime factors reads:
       15 = 3 x 5
    >>> f(100)
    The decomposition of 100 into prime factors reads:
       100 = 2^2 x 5^2
    >>> f(5432)
    The decomposition of 5432 into prime factors reads:
       5432 = 2^3 x 7 x 97
    >>> f(45103)
    The decomposition of 45103 into prime factors reads:
       45103 = 23 x 37 x 53
    >>> f(45100)
    The decomposition of 45100 into prime factors reads:
       45100 = 2^2 x 5^2 x 11 x 41
    '''
    factors = list()
    number = n
    while n % 2 == 0:
       factors.append(2)
       n = n // 2
    
    for d in range(3, int(sqrt(n))+1,2):
       while n % d == 0:
          factors.append(d)
          n = n // d
    if n > 2:
       factors.append(n)
    power = 1
    result = ''
    a = factors[0]
   #  print(factors)
    for f in factors[1:]:
       if f == a:
          power += 1
       else:
          if power == 1:
             result += str(a) + " x "
          else:
             result += str(a) + "^" + str(power) + " x "
          a = f
          power = 1
    if power > 1:
       result += str(a) + "^" + str(power)
    else:
       result += str(a)
      

    print(f'The decomposition of {number} into prime factors reads:')
    print(f'   {number} = {result}')
    # Insert your code here

    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
   # f(45100)
