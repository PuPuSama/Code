n = int(input())
a,b=[],[]
for i in range(n):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
print(a,b)
for i in range(1,10000):
    flag = 1
    for j in range(n):
        if a[j]//i!=b[j]:
            flag = 0
            break
    if flag == 1 :
        print(i,end=' ')
        break
for i in range(10000,1,-1):
    flag = 1
    for j in range(n):
        if a[j]//i!=b[j]:
            flag = 0
            break
    if flag == 1 :
        print(i)
        break