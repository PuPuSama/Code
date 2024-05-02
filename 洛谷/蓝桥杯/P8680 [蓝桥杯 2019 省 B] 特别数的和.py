n = int(input())
sum = 0
for i in range(1,n+1):
    if any(str(p) in '2019' for p in str(i)):
        sum = sum + i
print(sum)
        