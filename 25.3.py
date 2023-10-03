from random import*
a=[0]*12
sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
sum6=0
for i in range(12):
    a[i]=randint(1000,2000)
    print(a[i],end=' ')
print()
for k in range(0,6):
    sum1+=a[k]
print(f'Sale in First Half : {sum1}')
for j in range(6,12):
    sum2+=a[j]
print(f'Sale in Second Half : {sum2}')
for b in range(0,3):
    sum3+=a[b]
print(f'Sale in First Quarter : {sum3}')
for c in range(3,6):
    sum4+=a[k]
print(f'Sale in Second Quarter : {sum4}')
for d in range(6,9):
    sum5+=a[d]
print(f'Sale in Third Quarter : {sum5}')
for e in range(9,12):
    sum6+=a[e]
print(f'Sale in Fourth Quarter : {sum6}')