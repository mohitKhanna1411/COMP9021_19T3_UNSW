# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 7


'''
Will be tested with height a strictly positive integer.
'''


def f(height):
    '''
    >>> f(1)
    0
    >>> f(2)
     0
    123
    >>> f(3)
      0
     123
    45678
    >>> f(4)
       0
      123
     45678
    9012345
    >>> f(5)
        0
       123
      45678
     9012345
    678901234
    >>> f(6)
         0
        123
       45678
      9012345
     678901234
    56789012345
    >>> f(20)
                       0
                      123
                     45678
                    9012345
                   678901234
                  56789012345
                 6789012345678
                901234567890123
               45678901234567890
              1234567890123456789
             012345678901234567890
            12345678901234567890123
           4567890123456789012345678
          901234567890123456789012345
         67890123456789012345678901234
        5678901234567890123456789012345
       678901234567890123456789012345678
      90123456789012345678901234567890123
     4567890123456789012345678901234567890
    123456789012345678901234567890123456789
    '''
    # Insert your code here
    d=0
    for i in range(1,height+1):
        print(' '*(height-i),end='')
        for j in range((i-1)*2+1):
            print(d,end='')
            d=(d+1)%10               
        print()

if __name__ == '__main__':
    n = input("enter a number")
    no_zeros = 0
    i= 1
    print(n)
    while True:
        if n[-i] == '0':
            no_zeros += 1
        else:
            break
        i+=1
    print(no_zeros)
    # import doctest
    # doctest.testmod()