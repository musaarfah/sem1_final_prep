from random import*
len=int(input('Length :'))
a=[0]*len
sum =0
for i in range (len):
    a[i]=randint(1,100)
    print(a[i],end=' ')
    sum+=a[i]
print()
avg=sum//len
print('Average :',avg)
count_p=0
count_n=0
for j in range(len):
    a[i]=avg-a[i]
    print(a[i],end=' ')
    if a[i]>0:
       count_p+=1
    elif a[i]<0:
        count_n+=1
print()
print(f'Count of Positive Numbers : {count_p}')
print(f'Count of Negative Numbers : {count_n}')