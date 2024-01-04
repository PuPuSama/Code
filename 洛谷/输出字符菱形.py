n = int(input("请输入行数: "))
n = n // 2 + 1  # 将行数转换为对角线长度
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))