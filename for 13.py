rows=int(input('rows :'))
for i in range(1,rows+1):
    for j in range(i,rows):
        print(' ',end=' ')
        j=j+1
    print(i)
    i=i+1