i=1
count=0
while i<=4:
    j=1
    while j<=6:
        count=count+1
        print('*',end=' ')
        if count%6==0:
            print('>')
        j=j+1
    i=i+1