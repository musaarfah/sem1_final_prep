n=int(input('n :'))
k=int(input('k :'))
i=1
while i<=n:
    j=1
    while j<=k:
        if i == 1 and j == 1:
            print('{', end='')
        print(f'({i},{j})',end='')
        if i<n or j<k:
            print(',',end='')
        if i==n and j==k:
            print('}',end='')
        j=j+1
    i=i+1