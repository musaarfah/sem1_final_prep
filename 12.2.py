from random import*
LENGTH = randint(5,9)
d = [[randint(1,9) for i in range(LENGTH)] for j in range(LENGTH)]
for i in range(LENGTH):
    d[i][i]=0
print(d)

for i in range(8):
    random_i = randint(1,5)
    random_j = randint(1,5)
    d[random_i][random_j] = -1
print(d)


for i in range (LENGTH):
    for j in range(LENGTH):
        print(d[i][j],end='\t')
    print()
for i in range(LENGTH):
    direct_link=' '
    for j in range(LENGTH):
        if d[i][j] !=-1:
            direct_link +=' '+ str(j)
    print(f'city {i} has direct links {direct_link}')

for i in range(LENGTH):
    for j in range(LENGTH):
        count=0
        if d[i][j]==-1:
            for k in range(LENGTH):
                if k!=i and k!=j:
                    m=i
                    count+=1
        if count==1:
            print(f'{i} has indirect link with {j} via {k}')

