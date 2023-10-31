def sum(List):
    CList = []
    temp = 0
    for i in range(len(List)):
        temp = temp + List[i]
        CList.append(temp)
    return CList
result = sum([1, 2, 3])
print(result)