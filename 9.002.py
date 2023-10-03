n=int(input('n : '))
x=n*2-1
for i in range(1,n+1):
    for j in range(i):
        print(end=' ')
    print('*',end='')
    for k in range(x-i*2):
        print(end=' ')
    if i<n:
      print('*',end='')
    for l in range(1,i*2-2):
        print(end=' ')
    if i!=1:
      print('*',end='')
    for m in range(x-i*2):
        print(end=' ')
    if i<n:
      print('*',end='')
    print()