'homework problem 6.3'

def palidrone(word):
    if len(word) < 3:
        return False
    else:
        first = word[0]
        last = word[-1]
        middle = word[1:-1]
        rev_middle = ''
        for letter in middle:
            rev_middle = letter + rev_middle
        if first == last and middle == rev_middle:            
            return True
        else:
            return False

    
word = 'aba'
print(palidrone(word))


