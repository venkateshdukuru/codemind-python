_=int(input())
v=list(map(int,input().split()))
k=list(set(v))
k.sort()
for r in range(len(k)-1,-1,-1):
    if v.count(k[r])==1:
        print(k[r])
        break
else:
    print(-1)