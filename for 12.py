rows=int(input('rows :'))
i=1
for i in range(1,rows+1):
    for j in range(1,i):
        print(' ',end=' ')
        j=j+1
    print(i)
    i=i+1