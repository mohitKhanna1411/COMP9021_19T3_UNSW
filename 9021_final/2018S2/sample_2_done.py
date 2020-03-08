
def f(N):
    '''
    >>> f(20)
    Here are your banknotes:
    $20: 1
    >>> f(40)
    Here are your banknotes:
    $20: 2
    >>> f(42)
    Here are your banknotes:
    $2: 1
    $20: 2
    >>> f(43)
    Here are your banknotes:
    $1: 1
    $2: 1
    $20: 2
    >>> f(45)
    Here are your banknotes:
    $5: 1
    $20: 2
    >>> f(2537)
    Here are your banknotes:
    $2: 1
    $5: 1
    $10: 1
    $20: 1
    $100: 25
    '''
    banknote_values = [1, 2, 5, 10, 20, 50, 100]
    banknotes = dict.fromkeys(banknote_values, 0)
    # print(banknotes)
    # Insert your code here
    length = len(banknote_values) - 1
    while N > 0 and length >= 0:
        count,N = divmod(N,banknote_values[length])
        if count > 0:
            banknotes[banknote_values[length]] = count
        length -= 1
    print('Here are your banknotes:')
    for v in sorted(banknotes):
        if banknotes[v]:
            print(f'${v}: {banknotes[v]}')
                        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
