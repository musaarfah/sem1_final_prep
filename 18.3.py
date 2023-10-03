n=int(input('n : '))
'''
for i in range(n):
    for j in range (i):
        print(end=' ')
    for k in range(n-i):
        print('+',end='')
    print()
for i in range(1, n):
    for m in range(n - i - 1):
        print(end=' ')
    for n in range(i + 1):
        print('+',end='')
    print()
'''
for k in range(n):
    for l in range(k):
        print(end=' ')
    for m in range(n-k):
        print('+', end='')
    print()
for i in range(1,n):
    for j in range(n-i-1):
        print(end=' ')
    for j in range(i+1):
        print('+', end='')
    print()