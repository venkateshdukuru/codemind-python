n=int(input())
v=list(map(int,input().split()))
k=list(map(int,input().split()))
for i in range(n):
    print(v[i]+k[i],end=' ')