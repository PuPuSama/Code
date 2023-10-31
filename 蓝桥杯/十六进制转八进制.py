n = int(input())
lst = []
while len(lst)<n:
    temp = oct(int(input(), 16))
    temp = temp[2:]
    lst.append(temp)
for i in lst:
    print(i)
