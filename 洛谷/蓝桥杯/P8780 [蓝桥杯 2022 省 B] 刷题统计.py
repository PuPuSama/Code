a,b,n = map(int,input().split())
i = 1
while True:
    week = (i - 1) // 7 + 1  # 计算周数，从 1 开始计数
    day = (i - 1) % 7 + 1  # 计算天数，从 1 开始计数
    print("第", week, "周", "第", day, "天")
    if i % 7 <= 5:
        x = i % 7 * a
    else:
        x = ((i % 7)-5)*b + 5 * a
    x += (i // 7) * 5 * a + (i // 7) * 2 * b
  
    print(x)
    if x >= n:
        break
    i += 1
print(i)
