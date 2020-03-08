# You might find the ord() function useful.

def longest_leftmost_sequence_of_consecutive_letters(word):
    '''
    You can assume that "word" is a string of
    nothing but lowercase letters.
    
    >>> longest_leftmost_sequence_of_consecutive_letters('')
    ''
    >>> longest_leftmost_sequence_of_consecutive_letters('a')
    'a'
    >>> longest_leftmost_sequence_of_consecutive_letters('zuba')
    'z'
    >>> longest_leftmost_sequence_of_consecutive_letters('ab')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('bcab')
    'bc'
    >>> longest_leftmost_sequence_of_consecutive_letters('aabbccddee')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt')
    'xyz'
    >>> longest_leftmost_sequence_of_consecutive_letters('efghuvwijlrstuvabcde')
    'rstuv'
    '''
    result_arr = []
    final = []
    if word:
        first = list(word)[0]
        result_arr.append(first)

        for w in word[1:]:
            if ord(first) + 1 == ord(w):
                result_arr.append(w)
            else:
                if len(result_arr):
                    final.append(''.join(result_arr))
                    result_arr = []
                    result_arr.append(w)

            first = w
        if len(result_arr):
            final.append(''.join(result_arr))
        length = len(sorted(final,key=len)[-1])

        for i in sorted(final,key=len):
            if len(i) == length:
                print("'" + i + "'")
                break
    else:
        print("''")
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()
