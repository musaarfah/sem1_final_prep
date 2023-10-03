from random import *
def list_generate():
    length=10
    x=[0]*length
    for i in range(length):
        x[i]=randint(0,100)
        print(x[i],end=' ')
    print()
    return x

# x=list_generate()
# print('Pairs in Order :')
# for i in range(len(x)-1):
#     if x[i]<=x[i+1]:
#         print(x[i],' ',x[i+1])
#
# a=list_generate()
# b=list_generate()
# for i in range(len(a)-1):
#     if a[i]>b[i]:
#         print(a[i],end=' ')
#     else:
#         print(b[i],end=' ')


# print('List 1: ',end='')
# a=list_generate()
# print('List 2: ',end='')
# b=list_generate()
# for i in range(len(a)):
#     if a[i]>b[i]:
#         b[i]=a[i]
#     print(a[i],end=' ')
# print()
# for i in range(len(b)):
#     if b[i]<a[i]:
#         a[i]=b[i]
#     print(b[i],end=' ')





# a=list_generate()
# count=0
# for i in range(len(a)-1):
#     if a[i+1]>a[i]:
#         count+=1
# if count==len(a):
#     print('List is Sorted')
# else:
#     print('Not Sorted')