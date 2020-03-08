import sys
import math

def all_factors(n):

    list_factors = []
    while n % 2 == 0:
        list_factors.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            list_factors.append(int(i))
            n = n / i
    if n > 2:
        list_factors.append(int(n))

    print(list_factors)
    a = list_factors[0]
    fac = 1
    result = ''
    for i in list_factors[1:]:
        if a == i:
            fac += 1
        else:
            result += str(a) + '**' + str(fac) + ' * '
            fac = 1
            a = i
    result+= str(a) + '**' + str(fac) + ' * '
    
    print(result[:-2])

if __name__ == '__main__':
    
    all_factors(9 * 25 * 64)
