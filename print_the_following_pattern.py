n=int(input())
for r in range(1,n+1):
    for v in range(1,n-r+1):
        print(' ',end='')
    for k in range(1,2*r):
        print(abs(k-r),end='')
    print()