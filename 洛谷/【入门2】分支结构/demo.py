count = 0
for i in range(1,1000000):
    flag = 0  
    for j in range(1,i//2+1):
        if flag > 1:
            break
        if (i / j).is_integer() == True:
            flag += 1
    if flag == 1 :
        a = i//100000
        b = i//10000 - a * 10
        c = i//1000 - a * 100 - b * 10
        d = i//100 - a * 1000 - b * 100 - c * 10
        e = i//10 - a * 10000 - b * 1000 - c * 100 - d * 10
        f = i%10
        if(a+b+c+d+e+f == 23):
            print(i)
            count += 1
print(count)
 
        