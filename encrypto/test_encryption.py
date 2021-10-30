# verson 1.0
import random

def encrypt(t):
    en_text = ''+chr(en)
    for i in (ord(i) for i in t):
        i += en; en_text+=chr(i)
    print(en_text)
    return en_text

def decrypt(t):
    print('encrypted text found, decrypting')
    de_text = ''
    for i in (ord(i) for i in t[1:]):
        i -= ord(t[0]); de_text+=chr(i)
        # print(chr(i))
    print(de_text)
    return de_text

while True:
    en = random.randint(933, 1107)
    input_ = input('hit the keys and press enter: ')
    if ord(input_[0]) > 932:
        decrypt(input_)
    else: encrypt(input_)