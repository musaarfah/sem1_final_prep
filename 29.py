'''
st1=input('String 1:')
st2=input('String 2:')
st=''
for i in range(len(st1)):
    st= st+st1[i]
for i in range(len(st2)):
    st=st+st2[i]
print(st)
'''

name=input('Name :')
st1=''
st2=''
i=0
while name[i] != ' ':
    st1=st1+name[i]
    i+=1
i=0
while i<=len(name):
    print(st2)
# Task 7 (incomplete)
'''
a=[randint(1,15) for i in range(10)]
print(a)
b=[]
c=[]
d=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j] and i not in b:
            c.append(a[i])
            b.append(j)
            d.append(i)
print(c)
print(b)
print(d)
for i in range(len(c)):
    print(f'{c[i]} is present at indices {b[i]} {d[i]}')
'''
