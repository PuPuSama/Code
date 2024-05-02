n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
print(max(l))
print(min(l))
print(f"{sum(l)/n:.2f}")