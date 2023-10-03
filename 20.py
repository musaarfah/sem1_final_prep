def rectungular_box(rows,cols):
 for i in range(1,rows+1):
    if i==1 or i==rows:
        for j in range(cols):
            print('*',end='')
    else:
        for k in range(1):
            print('*',end='')
        for l in range(cols-2):
            print(end=' ')
        for m in range(1):
            print('*',end='')
    print()
rectungular_box(5,10)