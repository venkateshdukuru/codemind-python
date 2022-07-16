_=int(input())
v=list(map(int,input().split()))
k=list(set(v))
k.sort()
res=k[0]
l=0
for r in k:
    if v.count(r)>l:
        l=v.count(r)
        res=r
print(res)