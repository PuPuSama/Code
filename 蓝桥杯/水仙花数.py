n = int(input())
q = 3
for i in range(n):
    a = i//100
    b = i//10 - a*10
    c = i % 10
    if(a**q+b**q+c**q==i):
        print(i)
