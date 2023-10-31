def dec_to_X(num:int,x:int):
    s=''
    while num > 0:
        r = num % x
        if r > 9:
            r=chr(65+r-10)
        s=str(r) + s
        num = num // x
    return s
def X_dec_to_10(num:str,x:int):
    lst = list(num[::-1])
    temp = 0
    for j,i in enumerate(lst):
        if i >= 'A' and x > 10: 
            i = ord(i) - 65 + 10
        temp = temp + int(i)*x**j
    return temp 
print(dec_to_X(10,16))
print(X_dec_to_10('A5',16))