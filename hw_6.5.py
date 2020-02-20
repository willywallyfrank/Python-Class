def gcd(a,b):
    while b:
        r = a%b
        a, b = b, r
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

a = 72
b = 60

string1 = 'the gcd of {} and {} is {}'.format(a,b,gcd(a,b))
string2 = 'the lcm of {} and {} is {}'.format(a,b,lcm(a,b))

print(string1)
print(string2)
                                              


                                                      
                                                      
                                                      
