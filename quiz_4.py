# COMP9021 19T3 - Rachid Hamadi
# Quiz 4 *** Due Thursday Week 5
#
# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends
#   and around parentheses and commas, is a valid word.


import sys


def is_valid(word, arity):
    stack = []
    word = word.strip()
    for item in word:
        if not item.isalpha() and item not in ['_',' ','(',')',',']:
            return False
        if item == '(':
            stack.append(item)
        if item == ')':
            if len(stack):
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        return False

    if arity == 0:
        if word.find('(') > 0 or word.find(')') > 0:
            return False

    if arity > 0:
        if word.find('(') == -1 or word.find(')') == -1:
            return False
        closing_index = word.rindex(')')
        residue = word[closing_index+1:].strip()
        if len(residue):
            return False

        while word.find('(') > 0:
            right = word.index(')')
            left = word[:right].rindex('(')
            
            if right > -1 and left == -1:
                return False
            if right == -1 and left > -1:
                return False

            parameters = word[left + 1 : right].strip()
            list_parameters = parameters.split(',')
            
            if len(list_parameters) != arity:
                return False
            for parameter in list_parameters:
                if not parameter:
                    return False

            word = word[:left] + word[right + 1 :]
    
    word = word.strip()
    for item in word:
        if not item.isalpha() and item != '_':
            return False

    return True

try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')

