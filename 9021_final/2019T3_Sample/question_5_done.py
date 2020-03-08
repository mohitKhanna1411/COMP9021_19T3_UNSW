# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 5


'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''

import csv
#import numpy as np

def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    # Insert your code here
    csv_file = open('cpiai.csv')
    month_list = list()
    out = list()
    inflation = list()
    file_content = list(csv.reader(csv_file))
    for f in file_content:
        # print(str(f[0])[:4])
        if str(f[0])[:4] == str(year):
            month_list.append(f)

    for m in month_list:
        inflation.append(float(m[2]))
    
    max_inflation = max(inflation)

    for m in month_list:
        if m[2] == str(max_inflation):
            out.append(m[0].split('-')[1])
    month_dic = {'01':'Jan','02' : 'Feb','03':'Mar','04':'Apr','05':'May',
                '06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
    output = ''
    if len(out) == 1:
        print(f'In {year}, maximum inflation was: {max_inflation}')
        print(f'It was achieved in the following months: {month_dic[out[0]]}')
    if len(out) > 1:
        for o in out:
            output += month_dic[o] + ', '
        print(f'In {year}, maximum inflation was: {max_inflation}')
        print(f'It was achieved in the following months: {output[:-2]}')
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # f(1995)
