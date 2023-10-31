lst = list(map(int,input().split()))
print(*lst)
tlst = lst[:]
for i in range(len(lst)):
    for j in lst:
        tlst[i]=tlst[i]*j
print(*tlst)
    