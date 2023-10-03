from random import *
i=1
count_odd=0
count_even=0
for i in range(1,11):
    a=randint(1,10)
    print(a)
    if a%2==0:
        count_even=count_even+a
    if a%2!=0:
        count_odd=count_odd+a
print(f'Sum of odd numbers : {count_odd}')
print(f'Sum of even numbers : {count_even}')
