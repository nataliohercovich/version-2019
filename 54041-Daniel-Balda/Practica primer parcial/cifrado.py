import string
#crear un alfabeto
"""def create_abc():
    for letter in range(ord('a'),ord('z')+1):
        print(chr(letter))
"""

def encrypt(text, key): 
    abc = string.ascii_lowercase # space = ASCII -> 32
    x = ''
    aux = 0
    for letter in text:
        if letter == ' ':
            x += '%'
        else:
            position = aux % len(key)
            x += abc[int((abc.index(letter) + int(abc.index(key[position]))) % len(abc))]
            aux+=1
    return x