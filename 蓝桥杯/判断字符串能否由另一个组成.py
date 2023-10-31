def canConstruct(ransomNote: str, magazine: str):
    temp1 = list(ransomNote)
    temp2 = list(magazine)
    for i in range(len(ransomNote)):
        for j in range(len(magazine)):
            if temp1[i] == temp2[j]:
                temp1[i] = ''
                temp2[j] = ''
                break
    temp1 = [x for x in temp1 if x != '']
    if temp1 == []:
        return True
    else:
        return False
print(canConstruct('ab','aab'))