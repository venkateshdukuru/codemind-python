v=k=0
for i in range(int(input()),0,-1):
    v=k
    for j in range(1,i+1):
        v+=1
        print(v,end=' ')
    k+=1
    print()