n=int(input('enter the upper limit:'))
for i in range(1,n):
    if i%4==0 and i%8!=0:
        print(i,end='')