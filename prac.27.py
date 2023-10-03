from random import*
x = [23, 45, 18, 23, 17, 45, 36, 23, 45, 18, 36, 45, 18, 17, 36, 23, 17]
#
# SEN=-1
# for i in range (len(x)):
#     num=x[i]
#     if x[i]!=SEN:
#         print(num,end=' ')
#     for j in range(len(x)):
#         if x[j]==num:
#             x[j]=SEN

'''''
SEN=-1
y=[]
for i in range (len(x)):
    num=x[i]
    if x[i]!=SEN:
        print(num,end=' ')
        y.append(num)
    for j in range(len(x)):
        if x[j]==num:
            x[j]=SEN
print(y)
'''

SEN=-1
y=[]
z=[]
for i in range (len(x)):
    count = 1
    if x[i]!=SEN:
        print(x[i],end=' ')
        y.append(x[i])
    for j in range(i+1,len(x)):
        if x[j]==x[i]:
            x[j]=SEN
            count+=1
    z.append(count)

print(y)
print(z)

'''
x=[[randint(10,99) for j in range(3)] for i in range(4)]
for i in range(4):
    for j in range(3):
        print(x[i][j],end=' ')
print()
print()
for i in range(4):
    for j in range(3):
        print(x[i][j],end=' ')
    print()
print()
for i in range(3):
    for j in range(4):
        print(x[j][i],end=' ')
    print()
'''''

''''
x=[[randint(10,99) for j in range(4)] for i in range(4)]
for i in range(4):
    for j in range(4):
        print(x[i][j],end=' ')
print()
print('Primary diagnol elements : ',end=' ')
for i in range(4):
    for j in range(4):
        if i==j:
            print(x[i][j],end=' ')
print()
print('Secondary diagnol elements : ',end=' ')
for i in range(4):
    for j in range(4):
        if i+j==3:
            print(x[i][j],end=' ')
'''''
'''
x=[[randint(10,99) for j in range(3)] for i in range(4)]
for i in range(4):
    for j in range(3):
        print(x[i][j],end=' ')
print()
sum=0
for i in range(4):
    for j in range(3):
        print(x[i][j],end=' ')
        sum+=x[i][j]
    print(f'= {sum}')
    sum=0
'''