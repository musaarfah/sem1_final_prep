n=int(input('n :'))
for i in range(1,n+1):
    for j in range((n+1)-i):
        print(end=' ')
    for k in range(i,1,-1):
        print(k,end='')
    for l in range(1,i+1):
        print(l,end='')
    print()