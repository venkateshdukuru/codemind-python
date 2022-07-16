n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j==n or j==1 or i-j==0):
            print('*',end=' ')
        else:
            print(end='  ')
    print()