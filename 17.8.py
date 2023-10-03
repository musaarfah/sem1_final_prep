rows=int(input('rows :'))
i=1
while i<=rows:
    j=rows
    while j>i:
        print(' ',end=' ')
        j=j-1
    print(i)
    i=i+1
