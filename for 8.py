rows=int(input('rows :'))
cols=int(input('columns :'))
i=1
for i in range(1,rows+1):
    for j in range(1,cols+1):
        print(j,end=' ')
        j=j+1
    i=i+1
    print()