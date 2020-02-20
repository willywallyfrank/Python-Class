import math as m

def root(n):
    guess = 1
    tol = 10**-20
    diff = 1
    while diff > tol:
        new_guess = (guess + n/guess)/2
        diff = abs(guess - new_guess)
        guess = new_guess
    return guess


n = 2
square_root = root(n)
math_val = m.sqrt(n)
error = abs(square_root - math_val)

print('values for the square root of',n)
print('estimated: {0:.20f}'.format(square_root))
print('accepted:  {0:.20f}'.format(math_val))
print('error:     {0:.20f}'.format(error))
