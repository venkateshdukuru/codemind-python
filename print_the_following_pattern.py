n=int(input())
for i in range(n,0,-1):
    i=i+1
    for j in range(1,i):
        print(j,end='')
    print()