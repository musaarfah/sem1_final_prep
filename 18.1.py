n=int(input('n :'))
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end=' ')
        k=1
        while k<=i:
            print(' ',end=' ')
            k=k+1
        j=j+1
    print()
    i=i+1
