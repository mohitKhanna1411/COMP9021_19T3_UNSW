from math import factorial
result = list()
def nCr(n, r): 
  
    result.append( int((factorial(n) / (factorial(r)  
                * factorial(n - r)))) )

number = int(input("Input a number"))

for i in range(number):
    nCr(number - 1,i)
print(str(result).replace(',',''))