n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=[]
c=0
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    if a.count(i)==k:
        print(i,end=' ')
        c=1
if c==0:
    print('-1')