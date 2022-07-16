_=int(input())
v=list(map(int,input().split()))
k=[]
l=0
for r in v:
    if r==0:
        l+=1
        continue
    k.append(r)
for _ in range(l):
    k.append(0)
print(*k)