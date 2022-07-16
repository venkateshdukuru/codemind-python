for _ in range(int(input())):
    a=input()
    b=[]
    for i in a:
        b.append(int(i))
    if min(b)==max(b)-3:
        print('YES')
    else:
        print('NO')