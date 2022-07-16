_=int(input())
v=list(map(int,input().split()))
_=int(input())
k=list(map(int,input().split()))
r=int(input())
l=0
for i in range(len(v)):
    if v[i]<=r and r<=k[i]:
        l+=1
print(l)