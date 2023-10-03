n=int(input('n :'))
k=65
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(k),end=' ')
        k=k+1
        for l in range(1,j+1):
            print(l,end=' ')
    print()