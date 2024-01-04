'''
Author: PuPu 877770086@qq.com
Date: 2024-01-04 20:06:21
LastEditors: PuPu 877770086@qq.com
LastEditTime: 2024-01-04 20:12:32
FilePath: \洛谷\【入门1】顺序结构\B2029 大象喝水.py
Description: 
'''
h,r = map(int,input().split())
tmp = 3.14 * r * r * h
result = 20 / (tmp / 1000)
if result % 1 != 0:
    result = int(result) + 1
else:
    result = int(result)
print(result)