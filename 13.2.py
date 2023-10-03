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
print(f'Count of 1 : {count_of_1}')
print(f'Count of 2 : {count_of_2}')
print(f'Count of 3 : {count_of_3}')
print(f'Count of 4 : {count_of_4}')
print(f'Count of 5 : {count_of_5}')
print(f'Count of 6 : {count_of_6}')
print(f'Count of 7 : {count_of_7}')
print(f'Count of 8 : {count_of_8}')
print(f'Count of 9 : {count_of_9}')