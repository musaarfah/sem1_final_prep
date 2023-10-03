n=int(input('rows :'))
for i in range(1,n+1):
    for j in range(n+1-i):
        print(end=' ')
    for j in range(i,i+i):
        print(j,end='')
    for j in range(i+i-2,i-1,-1):
        print(j,end='')
    print()
'''
for i in range(1,n+1):
    for j in range(n*2-i*2):
        print(end=' ')
    print('*',end='')
    for j in range(4*(i-1)):
        print(end=' ')
    if i>1:
        print('*',end='')
    print()
'''
# for i in range(1,n):
#     for j in range(97,(97+n*i)+1,i):
#         print(chr(j),end=' ')
#     print()

# for i in range(1,n+1):
#     for j in range(n+1-i):
#         print(end=' ')
#     for j in range(1,i):
#         print(i+j-1,end='')
#     print()