from random import*
len=int(input('Length :'))
a=[0]*len
sum_pass=0
count_pass=0
for i in range(len):
    a[i]=randint(1,100)
    if a[i]>50:
        sum_pass+=a[i]
        count_pass+=1
    print(a[i],end=' ')
print()
avg_pass=sum_pass//count_pass
print('Average :',avg_pass)
for j in range(len):
    if a[j]<50:
        print(a[j],end=' ')
print()
for k in range(len):
    if a[k]>avg_pass:
        print(a[k],end=' ')
print()
for b in range(len):
    if a[b]<avg_pass:
        print(a[b],end=' ')