tmp = float(input())
if tmp >= 100 and tmp<1000:
    tmp = str(tmp)
    tmp = tmp[::-1]
    tmp = float(tmp)
print(tmp)