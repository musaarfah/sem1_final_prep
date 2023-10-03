rows =int(input('rows :'))
cols =int(input('columns :'))
jump=1
for i in range(rows):
    sum=0
    k=1
    for j in range(1,cols+1):
        print(k,end='')
        sum=sum+k
        if j<cols:
            print('+',end='')
        k=k+jump
    print(f'={sum}')
    jump=jump+1