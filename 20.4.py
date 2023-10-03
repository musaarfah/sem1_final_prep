def mid_value(a,b,c):
    mid =b
    if (b>a and a>c) or (c>a and a>b):
        mid=a
    if (c>a and c<b) or (c>b and c<a):
        mid=c
    print(mid)

mid_value(5,1,7)