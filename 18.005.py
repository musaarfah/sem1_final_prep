n=int(input('n :'))
for i in range(n):
    for j in range(i):
        print(end=' ')
    for k in range(n-i):
        print('+',end='')
    print()
for l in range(1,n):
    for m in range(n-l-1):
        print(end=' ')
    for p in range(l+1):
        print('+',end='')
    print()