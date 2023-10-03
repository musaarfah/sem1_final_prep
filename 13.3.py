file=open('nums.txt','r')
count_of_1=0
count_of_2=0
count_of_3=0
count_of_4=0
count_of_5=0
count_of_6=0
count_of_7=0
count_of_8=0
count_of_9=0
i=1
while i<=10000:
    line=int(file.readline())
    if line ==1:
        count_of_1=count_of_1+1
    if line ==2:
        count_of_2=count_of_2+1
    if line ==3:
        count_of_3=count_of_3+1
    if line ==4:
        count_of_4=count_of_4+1
    if line ==5:
        count_of_5=count_of_5+1
    if line ==6:
        count_of_6=count_of_6+1
    if line ==7:
        count_of_7=count_of_7+1
    if line ==8:
        count_of_8=count_of_8+1
    if line ==9:
        count_of_9=count_of_9+1
    i=i+1
file=open('counts.txt','w')
line=file.write(f'{count_of_1}\n')
line=file.write(f'{count_of_2}\n')
line=file.write(f'{count_of_3}\n')
line=file.write(f'{count_of_4}\n')
line=file.write(f'{count_of_5}\n')
line=file.write(f'{count_of_6}\n')
line=file.write(f'{count_of_7}\n')
line=file.write(f'{count_of_8}\n')
line=file.write(f'{count_of_9}')

