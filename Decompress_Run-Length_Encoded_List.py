_=int(input())
v=list(map(int,input().split()))
for i in range(0,len(v),2):
    for _ in range(v[i]):
        print(v[i+1],end=' ')