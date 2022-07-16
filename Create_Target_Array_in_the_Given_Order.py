_=int(input())
v=list(map(int,input().split()))
_=int(input())
k=list(map(int,input().split()))
r=[]
for i in range(len(v)):
    r.insert(k[i],v[i])
print(*r)