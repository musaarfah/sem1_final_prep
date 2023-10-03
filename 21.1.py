'''
import random
a=random.randint(1,10)
b=random.randint(1,10)
while a==b:
    b=random.randint(1,10)
c=random.randint(1,10)
while c==a or c==b:
    c=random.randint(1,10)
print(a,b,c)
'''

'''
from random import*
a=randint(2,100)
b=randint(2,100)
while a%b!=0 or a==b:
  b=randint(2,100)
print(a,b)
'''
'''
from random import*
a=randint(1,50)
b=randint(1,50)
count=0
while a+b!=50:
    a=randint(1,50)
    b=randint(1,50)
    count=count+1
print(a,b)
print(count)
'''

'''
from random import*
for i in range(5):
    a=randint(65,90)
    while a==65 or a==69 or a==73 or a==79 or a==85:
        a=randint(65,90)
    print(chr(a),end='')
'''

'''
from random import*
a=randint(1,10)
print(a)
for i in range(1,10):
    b=randint(2,3)
    a=a+b
    print(a)
'''
'''
from random import*
sum=0
while sum!=50:
    for i in range(10):
        a=randint(1,10)
        print(a,end='')
        sum=sum+a
    if sum!=50:
        print()
    else:
        print(sum)
        break
'''
'''
n=int(input('n :'))
for i in range(1,n+1):
    for j in range(i):
        print(end=' ')
    print('\\')
for k in range(n+2):
    print(end=' ')
for l in range(n):
    print('_',end='')
print()
for m in range(n):
    for a in range(n-m):
        print(end=' ')
    print('/')
'''



