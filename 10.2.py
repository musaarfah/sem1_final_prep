from random import*
c=[0]*10
score=0
for k in range(len(c)):
 a=[0]*10
 for i in range(len(a)):
    a[i]=randint(1,9)
 b=[0]*10
 for j in range(len(b)):
    b[i]=randint(1,9)
 print(f'{a[i]}+{b[j]}=',end=' ')
 x=int(input(' '))
 if x==a[i] +b[j]:
     score+=1

print(f'Score : {score}/10')

