n=int(input('n :'))
count=0
for i in range (1,n+1):
    k=97
    for j in range(i):
        print(chr(k),end=' ')
        k=k+1
        count=count+1
        if count%5==0:
            print()