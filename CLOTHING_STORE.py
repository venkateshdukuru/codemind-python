_=int(input())
v=list(map(int,input().split()))
k=set(v)
r=0
for i in k:
    r+=(v.count(i))//2
print(r)