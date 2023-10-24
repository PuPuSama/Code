def compare(str1,str2):
    if(len(str1)!=len(str2)):
        return 1
    else:
        if str1==str2:
            return 2
        str11=str1.upper()
        str22=str2.upper()
        if str11==str22:
            return 3
        else:
            return 4
str1,str2=input().split()
print(compare(str1,str2))
        