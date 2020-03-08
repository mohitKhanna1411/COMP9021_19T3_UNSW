# ord(c) returns the encoding of character c.
# chr(e) returns the character encoded by e.


def rectangle(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when z is reached.
    
    >>> rectangle(1, 1)
    a
    >>> rectangle(2, 3)
    ab
    dc
    ef
    >>> rectangle(3, 2)
    abc
    fed
    >>> rectangle(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''
    a = 97
    word_arr = []
    for i in range(height):
        for j in range(width):
            word_arr.append(chr(a))
            a +=1
            if a == 123:
                a = 97
        if i % 2 == 0:
            print(''.join(word_arr))
        else:
            print(''.join(reversed(word_arr)))
        word_arr = []
    # print(word_arr)
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE

if __name__ == '__main__':
    import doctest
    doctest.testmod()
