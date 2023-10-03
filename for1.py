from random import*
i=1
for i in range(1,11):
    a=randint(65,91)
    print(chr(a))
    if a==65 or a==69 or a==73 or a==78 or a==85:
        print('Alphabet is a Vowel')
    else:
        print('Alphabet is consonant')