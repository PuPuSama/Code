def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 测试斐波那契数列的前 10 项
for i in range(2,15):
    print("{}+{}={}".format(fibonacci(i-2),fibonacci(i-1),fibonacci(i)))