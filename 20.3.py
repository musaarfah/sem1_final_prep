def rand_nums(n,a,b):
    for i in range(n):
        x=randint(a,b)
        print(x,end=' ')

from random import *
rand_nums(5,50,100)