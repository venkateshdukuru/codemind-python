n=int(input())
a=list(map(int,input().split()))
a=set(a)
a=list(a)
s=0
for i in a:
    if i%2==0:
        s+=1
print(s)