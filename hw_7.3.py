from math import *

def pi_approx(n):
    constant = 2*sqrt(2)/9801
    summation = 0
    for k in range(n):
        term = factorial(4*k)*(1103 + 26390*k)/(factorial(k)**4*396**(4*k))
        summation += term
    val = 1/(constant*summation)
    return(val)
   

n = 1
print('{0:.50f}'.format(pi))
print('{0:.50f}'.format(pi_approx(n)))


        
