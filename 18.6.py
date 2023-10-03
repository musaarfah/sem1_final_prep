r=int(input('rows : '))
m=int(input('m : '))
for i in range (1,r*c,c):
    for j in range(1,c+1):
        print(m*j, end=' ')
    print()