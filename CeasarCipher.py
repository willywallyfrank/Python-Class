'''
Ceasar Shift Cipher
'''
from tkinter import filedialog
from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename

def menu():
    print('''
          Menu
          1. Encrypt Text
          2. Decrypt Text
          3. Quit
         ''')
    choice = input('Choice #: ')
    return choice

def open_file():
    root = Tk()
    filename = askopenfilename()
    root.withdraw()
    with open(filename,'r') as infile:
        text = infile.read()
    return text

def save_file(text):
    root = Tk()
    filename = asksaveasfilename()
    root.withdraw()
    if '.txt' not in filename:        
        filename += '.txt'
    with open(filename,'w') as outfile:            
        outfile.write(text)

def clean_text(text):
    clean_text = ''
    for character in text:
        if 31 < ord(character) < 127:
            clean_text += character
    return clean_text

def ceasar(text, mode):
    text = clean_text(text)
    key = int(input('Enter Key: '))
    if mode == 'decrypt':
        key *= -1
    newtext = ''
    for character in text:
        newval = (ord(character) + key -32)%95
        newtext += chr(newval + 32)
    return newtext

if __name__ == "__main__":
    repeat = True
    while repeat:
        choice = int(menu())
        if choice == 3:
            repeat = False
        if choice == 1:
            print('choose plain text file')
            pText = open_file()
            cText = ceasar(pText, 'encrypt')
            print('save cipher text as:')
            save_file(cText)
        if choice == 2:
            print('choose cypher text file')
            cText = open_file()
            dText = ceasar(cText, 'decrypt')
            print('save decipher text as:')
            save_file(dText)


