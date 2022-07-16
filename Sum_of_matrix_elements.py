a=int(input())
b=int(input())
d=0
for _ in range(0,a):
    d+=sum(list(map(int,input().split())))
print(d)