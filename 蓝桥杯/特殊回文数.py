n = int(input())
for i in range(10000,1000001):
    lst = [int(digtal) for digtal in str(i)]
    s = sum(lst)
    x=0
    y=len(lst)-1
    while x<y:
        if lst[x] == lst[y]:
            x = x + 1
            y = y - 1
        else:
            break
    if x >= y and s == n:
        print(i)        
    
