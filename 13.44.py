file3=open('counts.txt','r')
i=1
count=0
while i<=9:
    line=int(file3.readline())
    count=count+line
    i=i+1
print(count)
if count==10000:
    print('Count is 10000')
