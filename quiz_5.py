# COMP9021 19T3 - Rachid Hamadi
# Quiz 5 *** Due Thursday Week 7
#
# Implements a function that, based on the encoding of
# a single strictly positive integer that in base 2,
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, encodes
# a sequence of strictly positive integers N_1 ... N_k
# with k >= 1 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
#
# Implements a function to decode a positive integer N
# into a sequence of (one or more) strictly positive
# integers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.


import sys
from collections import deque


def encode(list_of_integers):
    binary_numbers = []
    for integer in list_of_integers:
        binary_numbers.append("".join([binary_digit * 2 for binary_digit in bin(integer)[2:]]))

    return int("0".join(binary_numbers), 2)    


def decode(integer):
    binary_number = bin(integer)[2:]

    if binary_number.count("1") % 2 == 1:
        return None

    binary_deque = deque(bin(integer)[2:])
    binary_string = ''

    while len(binary_deque) >= 2:
        first = binary_deque.popleft()
        second = binary_deque.popleft()
        if first == second:
            binary_string += first
        else:
            binary_string += ' '
            binary_deque.appendleft(second)

    result = [int(n, 2) for n in binary_string.split()]

    if len(binary_deque) == 0 and result:
        return result
    else:
        return None


# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))
if type(the_input) is int:
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2 :])
    decoding = decode(the_input)
    if decoding is None:
        print('Incorrect encoding!')
    else:
        print('  It encodes: ', decode(the_input))
else:
    print('  In base 2,', the_input, 'reads as',
          f'[{", ".join(bin(e)[2: ] for e in the_input)}]'
         )
    print('  It is encoded by', encode(the_input))
