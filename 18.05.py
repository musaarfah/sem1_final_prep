n=int(input('n :'))
for i in range(n):
    for j in range(n,i,-1):
        print('+',end='')
    print()
for k in range(1,n):
    for l in range(k+1):
        print('+',end='')
    print()