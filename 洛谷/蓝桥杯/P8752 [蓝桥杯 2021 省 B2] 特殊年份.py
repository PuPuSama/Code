'''
Author: PuPu 877770086@qq.com
Date: 2024-04-02 17:29:12
LastEditors: PuPu 877770086@qq.com
LastEditTime: 2024-04-02 17:42:29
FilePath: \Code\洛谷\蓝桥杯\P8752 [蓝桥杯 2021 省 B2] 特殊年份.py
Description: 
'''
l = []
count = 0   
for i in range(5):
    l.append(int(input()))
for i in l:
   s = [int (j) for j in str(i)]
   if s[0] == s[2] and s[1]+1 == s[3]:
       count += 1
print(count)
        