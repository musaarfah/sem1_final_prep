rows=int(input('rows :'))
cols=int(input('columns :'))
i=1
while i<=rows:
    j=i
    while j<=cols+(i-1):
        print(j,end=' ')
        j=j+1
    i=i+1
    print()