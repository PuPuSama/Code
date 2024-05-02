'''
Author: PuPu 877770086@qq.com
Date: 2024-04-02 16:31:54
LastEditors: PuPu 877770086@qq.com
LastEditTime: 2024-04-02 17:24:57
FilePath: \Code\洛谷\蓝桥杯\P8598 [蓝桥杯 2013 省 AB] 错误票据.py
Description: 
'''
n = int(input())
temp = []
x,y = 0,0
for i in range(n):
    m=list(map(int,input().split()))
    temp = temp + m
temp.sort()
for i in range(len(temp)-1):
    if temp[i] == temp[i+1]-2:
        x = temp[i]+1
    elif temp[i] == temp[i+1]:
        y = temp[i]
print(x,y)
