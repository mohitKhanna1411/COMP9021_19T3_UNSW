from itertools import *
'''
Given a word w, a good subsequence of w is defined as a word w' such that
- all letters in w' are different;
- w' is obtained from w by deleting some letters in w.

Returns the list of all good subsequences, without duplicates, in lexicographic order
(recall that the sorted() function sorts strings in lexicographic order).

The number of good sequences grows exponentially in the number of distinct letters in w,
so the function will be tested only for cases where the latter is not too large.

'''


def good_subsequences(word):
   '''
   >>> good_subsequences('')
   ['']
   >>> good_subsequences('aaa')
   ['', 'a']
   >>> good_subsequences('aaabbb')
   ['', 'a', 'ab', 'b']
   >>> good_subsequences('aaabbc')
   ['', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
   >>> good_subsequences('aaabbaaa')
   ['', 'a', 'ab', 'b', 'ba']
   >>> good_subsequences('abbbcaaabccc')
   ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac', 'bc', 'bca', 'c', 'ca', 'cab', 'cb']
   >>> good_subsequences('abbbcaaabcccaaa')
   ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac', 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
   >>> good_subsequences('abbbcaaabcccaaabbbbbccab')
   ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac', 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
   '''
   # Insert your code here
   word_set = [w[0] for w in groupby(word)]
   # print(word_set)
   out = ''
   result = []
   for length in range(len(word_set)+1):
      for w in combinations(''.join(word_set),length):
         if len(w) == len(set(w)):
            out = "'" + "".join(w) + "'"
            result.append(out)
   print(str(sorted(set(result))).replace('"',''))

   # Possibly define another function
                

if __name__ == '__main__':
    import doctest
    doctest.testmod()
   # good_subsequences('abbbcaaabcccaaabbbbbccab')
