s = input()
s1 = ''
for i in range(len(s)):
    if s[i].isalpha():
        s1 = s1 + s[i]
        if i < len(s) - 1 and s[i+1].isdigit():
            s1 = s1 + (int(s[i+1])-1) * s[i]
print(s1)