n = int(input())
l = []
while n != 0:
    l.append(n)
    n = n // 2
for i in range(len(l)):
    print(l[i],end=' ')
