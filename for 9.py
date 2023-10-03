rows=int(input('rows :'))
cols=int(input('columns :'))
i=1
for i in range(1,rows+1):
    for j in range (1,cols+1):
        if i==1 and j==1:
            print('{',end=' ')
        print(f'({i},{j})',end=' ')
        if i<rows or j<cols:
            print(',',end=' ')
        if i==rows and j==cols:
            print('}',end=' ')
        j=j+1
    i=i+1