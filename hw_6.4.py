#homework 6.4

def is_power(a, b):
    c = a/b
#    print(a,b,c)
    if c == 1:
        return True
    if a%b == 0 and is_power(c, b):
        return True
    else:
        return False
    
print(is_power(54,2))
