file=open('nums.txt','r')
i=1
count=0
while i<=10000:
    line=int(file.readline())
    count=count+line
    i=i+1
average=count/10000
print(average)