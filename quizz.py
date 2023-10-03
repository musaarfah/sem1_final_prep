n=int(input('n :'))
'''
for i in range(1,n+1):
    for j in range(97,97+n*i,i):
        print(chr(j),end='')
    print()
    for k in range(1,n*i,i):
        print(k,end='')
    print()
'''
for i in range(1,n+1):
    for j in range(97, 97+n*i,i):
        print(chr(j), end='')
    print()
    for j in range(1,n*i,i):
        print(j, end='')
    print()