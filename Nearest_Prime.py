t=int(input())
while t:
    a=int(input())
    temp=a
    while True:
        for j in range(2,int(a**0.5)+1):
            if(a%j==0):
                break
        else:
            np=a
            break
        a+=1
    a=temp
    while a:
        for j in range(2,int(a**0.5)+1):
            if(a%j==0):
                break
        else:
            pp=a
            break
        a-=1
    a=temp
    if(abs(np-a)<abs(pp-a)):
        print(np)
    elif(abs(np-a)>abs(pp-a)):
        print(pp)
    else:
        print(pp)
    t-=1
    