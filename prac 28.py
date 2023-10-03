from random import*

# Task1,2,3
'''
x=[randint(1,100) for i in range(10)]
print(x)
print(x[::-1])
sum=0
for i in range(10):
    sum+=x[i]
print(sum)
y=[x[i] for i in range(len(x))]
print(y)
'''

# Task 4
''''
a=[randint(1,50) for i in range(5)]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
b=[randint(1,50) for i in range(5)]
for i in range(len(b)-1):
    for j in range(len(b)-1):
        if b[j]>b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
print(b)
c=[]
for i in range(5):
    c.append(a[i])
    c.append(b[i])
print(c)
for i in range (len(c)-1):
    for j in range(len(c)-1):
        if c[j]>c[j+1]:
            c[j],c[j+1]=c[j+1],c[j]
print(c)
'''''

# Task 5
'''
a=[randint(1,50) for i in range(10)]
print(a)
count_even=0
b=[]
for i in range(len(a)):
    if a[i]%2==0:
        b.append(a[i])
        count_even+=1
count_odd=0
c=[]
for i in range(len(a)):
    if a[i]%2!=0:
        c.append(a[i])
        count_odd+=1
print(b)
print(c)
print(f'Count Odd : {count_odd}')
print(f'Count Even : {count_even}')
if count_odd>count_even:
    for i in range (len(b)):
        b[i]=b[i]-1
print(b)
if count_even>count_odd:
    for i in range (len(c)):
        c[i]=c[i]+1
print(c)
'''''

# Task 6
''''
a=[]
for i in range(10):
    num=randint(1,15)
    if num not in a:
        a.append(num)
print(a)
'''
# TASK 7
'''
a = [randint(1,5) for i in range(10)]
print(a)
print('Indexes of same element')
for i in range(len(a)):
    if a[i]!=-1:
        print()
        print(f'{a[i]} are : {i}',end=' ')
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                print(j,end=' ')
                a[j]=-1
'''

# Task 8
'''
a=[]
for i in range(20):
    num=randint(1,100)
    if num not in a:
        a.append(num)
print(a)
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
for i in range(1,max(a)):
    if i not in a:
        print(i,end=' ')
'''
# Task 9
'''
a=[randint(0,9)for i in range(20)]
print(a)
for i in range(2,len(a)-2):
    x=(a[i-2]+a[i-1]+a[i+1]+a[i+2])//4
    a[i]=x
print(a)
'''

# Task 10
'''
a=[randint(3,7) for i in range(10)]
print(a)
for i in range(len(a)):
    for j in range(a[i]):
        print('*',end='')
    print()
'''

# Task 11
'''
a=[randint(3,7) for i in range(10)]
print(a)
for i in range(len(a)):
    for j in range(i):
        print(a[j],end=' ')
    print()
'''

# Task 12
'''
a=[randint(3,7) for i in range(10)]
print(a)
for i in range(len(a)):
    sum=0
    for j in range(i):
        print(a[j],end=' ')
        sum+=a[j]
    if sum>0:
     print('=',sum)
'''

# Task 13
'''
a=[randint(3,7) for i in range(10)]
print(a)
for i in range(10):
    for j in range(i,i+3):
        if i+3<=10:
         print(a[j],end=' ')
    print()
'''

# Task 14
''''
a=[[randint(0,9) for j in range(10)]for i in range(10)]
for i in range(10):
    for j in range(10):
        print(a[i][j],end=' ')
    print()
for i in range(10):
    for j in range(10):
        if a[i]==a[j]:
            for k in range(j):
                print(end=' ')
            print(a[i][j])
for i in range(10):
    for j in range(10):
        if a[i][j]==0:
            a[i][j]=1
        print(a[i][j],end=' ')
    print()
'''''

# Task 15
'''
a=[[randint(0,9) for j in range(10)]for i in range(10)]
for i in range(10):
    for j in range(10):
        print(a[i][j],end=' ')
    print()
for i in range(10):
    for j in range(10):
        if a[i][j]==0:
            print(i,j)
print()
'''
a=[randint(0,9) for i in range(100)]
print(a)