n=int(input('n :'))
for i in range(n):
    for j in range(n,i,-1):
        print('+',end='')
    for k in range(i+i):
        print(end=' ')
    for l in range(n-i):
        print('+',end='')
    print()
for a in range(1,n):
    for b in range(a+1):
        print('+',end='')
    for c in range((n-a-1)+(n-a-1)):
        print(end=' ')
    for d in range(a+1):
        print('+',end='')
    print()