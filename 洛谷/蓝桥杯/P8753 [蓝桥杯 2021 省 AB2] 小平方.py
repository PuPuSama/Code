n = int(input())
count = 0
for i in range(1,n):
   if (i * i) % n < n/2:
      count += 1
print(count)