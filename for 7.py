n=int(input('n :'))
k=int(input('k :'))
i=1
for i in range (1,n+1):
    for j in range(1,k+1):
        print(f'{i}     {j}')
        j=j+1
    i=i+1