n=int(input('n :'))
for i in range(1,n+1):
    for j in range(n+n+1):
        print('+',end=' ')
    print()
    for k in range(1,n):
        print('+',end=' ')
    for l in range(i+i):
        print(' ',end=' ')
    for m in range(1,n):
        print('+',end=' ')
    print()