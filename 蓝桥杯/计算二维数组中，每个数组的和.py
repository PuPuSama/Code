def max_sum(accounts:list[list]):
    max = 0
    for i in range(0,len(accounts)):
        temp = sum(accounts[i])
        if temp > max:
            max =temp
    return max
print(max_sum([[1,2,3],[3,2,1]]))
    

        