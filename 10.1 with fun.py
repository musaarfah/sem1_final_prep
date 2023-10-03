from random import*


def find_min(start,end):
    for k in range (start,end):
     if k==start:
        min=a[k]
     elif min>a[k]:
        min=a[k]
    return min


def find_max(n,m):
    for k in range(n,m):
     if k == n:
        max = a[n]
     elif a[k]>max:
        max = a[k]
    return max


def find_avg(sum):
    avg=sum//3
    return avg

a=[0]*12
print('Monthly Sales :',end=' ')
for i in range(len(a)):
    a[i]=randint(10,99)
    print(a[i],end=' ')
print()
print('Quarter 1 :',end='\t')
sum1=0
for j in range(3):
    print(a[j],end=' ')
    sum1+=a[j]
min1=find_min(0,3);    max1=find_max(0,3);
print(f'\tMin : {min1}\tMax : {max1}',end='\t')
avg1=find_avg(sum1)
print('Average :',avg1)
print('Quarter 2 :',end='\t')
sum2=0
for j in range(3,6):
    print(a[j],end=' ')
    sum2+=a[j]
min2=find_min(3,6);    max2=find_max(3,6);
print(f'\tMin : {min2}\tMax : {max2}',end='\t')
avg2=find_avg(sum2)
print('Average :',avg2)
print('Quarter 3 :',end='\t')
sum3=0
for j in range(6,9):
    print(a[j],end=' ')
    sum3+=a[j]
min3=find_min(6,9);    max3=find_max(6,9);
print(f'\tMin : {min3}\tMax : {max3}',end='\t')
avg3=find_avg(sum3)
print('Average :',avg3)
print('Quarter 4 :',end='\t')
sum4=0
for j in range(9,12):
    print(a[j],end=' ')
    sum4+=a[j]
min4=find_min(9,12);    max4=find_max(9,12);
print(f'\tMin : {min4}\tMax : {max4}',end='\t')
avg4=find_avg(sum4)
print('Average :',avg4)
min=min1
if min2<min:
    min=min2
elif min3<min:
    min=min3
elif min4<min:
    min4=min
print(f'Q')

