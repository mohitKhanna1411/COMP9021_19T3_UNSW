

def f(word):
    '''
    Recall that if c is an ascii character then ord(c) returns its ascii code.
    Will be tested on nonempty strings of lowercase letters only.

    >>> f('x')
    The longest substring of consecutive letters has a length of 1.
    The leftmost such substring is x.
    >>> f('xy')
    The longest substring of consecutive letters has a length of 2.
    The leftmost such substring is xy.
    >>> f('ababcuvwaba')
    The longest substring of consecutive letters has a length of 3.
    The leftmost such substring is abc.
    >>> f('abbcedffghiefghiaaabbcdefgg')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is bcdefg.
    >>> f('abcabccdefcdefghacdef')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is cdefgh.
    '''
    sub_word = []
    result = list()
    first = word[:1]
    sub_word.append(first)
    for w in word[1:]:
        
        if ord(first) + 1 == ord(w):
            sub_word.append(w)
        else:
            if len(sub_word):
                result.append(''.join(sub_word))
                sub_word = []
                sub_word.append(w)
        first = w
    if len(sub_word):
        result.append(''.join(sub_word))
    length_wise = len(sorted(result, key=len)[-1])
    for i in sorted(result, key=len):
        if len(i) == length_wise:
            print(f'The longest substring of consecutive letters has a length of {len(i)}.')
            print(f'The leftmost such substring is {i}.')
            break
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # f('abbcedffghiefghiaaabbcdefgg')
