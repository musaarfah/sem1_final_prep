from random import*
a=[0]*12
print('Monthly Sales :',end=' ')
for i in range(len(a)):
    a[i]=randint(10,99)
    print(a[i],end=' ')
print()
print('Quarter 1 :',end=' ')
sum1=0
sum2=0
sum3=0
sum4=0
for j in range(3):
    print(a[j],end=' ')
    sum1+=a[j]
    if j==0:
        min=a[j]
    elif min>a[j]:
        min=a[j]
    if j==0:
        max=a[j]
    elif max<a[j]:
        max=a[j]
print(f'\t Min : {min},\t Max : {max}',end='\t')
avg1=int(sum1/3)
print('Average :',avg1)
print('Quarter 2 :',end=' ')
for k in range(3,6):
    print(a[k],end=' ')
    sum2+=a[k]
    if k==3:
        min1=a[k]
    elif min1>a[k]:
        min1=a[k]
    if k==3:
        max1=a[k]
    elif max1<a[k]:
        max1=a[k]
print(f'\t Min : {min1} \t Max : {max1}',end='\t')
avg2=int(sum2/3)
print('Average :',avg2)
print('Quarter 3 :',end=' ')
for l in range(6,9):
    print(a[l],end=' ')
    sum3+=a[l]
    if l==6:
        min2=a[l]
    elif min2>a[l]:
        min2=a[l]
    if l==6:
        max2=a[l]
    elif max2<a[l]:
        max2=a[l]
print(f'\t Min : {min2} \t Max : {max2}',end='\t')
avg3=int(sum3/3)
print('Average :',avg3)
print('Quarter 4 :',end=' ')
for m in range(9,12):
    print(a[m],end=' ')
    sum4+=a[m]
    if m==9:
        min3=a[m]
    elif min3>a[m]:
        min3=a[m]
    if m==9:
        max3=a[m]
    elif max3<a[m]:
        max3=a[m]
print(f'\t Min : {min3} \t Max : {max3}',end='\t')
avg4=int(sum4/3)
print('Average :',avg4)