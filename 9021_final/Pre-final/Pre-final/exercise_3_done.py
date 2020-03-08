import time
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
    if number==2:
        return 2
    pn=[]
    for i in [2,3,5,7,11]:
        if number%i==0:
            j=1
            while number%(i**j)==0:
                j=j+1
            number,r=divmod(number,i**(j-1))
            if i not in pn:
                pn.append(i)
    while number!=1:
        n=0
        for i in range(13,number,2):
            
            if number%i==0:
                n+=1
                j=1
                while number%(i**j)==0:
                    j=j+1
                number,r=divmod(number,i**(j-1))
                if i not in pn:
                    pn.append(i)
                break
        pp=[2,3,5,7,11]
        if number!=1:
                
            n=0
            for i in range(13,int(number**0.5)+1,2):
                if number%i==0:
                    n+=1
                    break
            if n==0:
                pn.append(number)
                number=1
            
            
            
            
    
    r=1
    for i in pn:
        r=r*i
    if r != 1:
        return r
        
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()
