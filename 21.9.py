n=int(input('n :'))
for i in range(1,(n*2)+1):
    if i==1:
        for j in range(n*2):
            print('*',end='')
print()
for k in range(1,n):
        for a in range(k):
            print('o',end='')
        for b in range((n*2)-(2*k)):
            print('*',end='')
        for c in range (k):
            print('o',end='')
        print()
for l in range(1,n):
        for d in range(n-l):
            print('o',end='')
        for e in range(2*l):
            print('*',end='')
        for f in range(n-l):
            print('o',end='')
        print()
for i in range(1,(n*2)+1):
    if i==n*2:
        for j in range(n*2):
            print('*',end='')