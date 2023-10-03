n=int(input('n :'))
for i in range (n):
    for j in range(i):
        print(end=' ')
    print('|_',end='')
    for k in range((n-i)*2-2):
        print(end=' ')
    if i<n-1:
        print('_|',end='')
    else:
      print('|',end='')
    print()