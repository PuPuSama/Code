'''
Author: PuPu 877770086@qq.com
Date: 2024-01-04 18:01:30
LastEditors: PuPu 877770086@qq.com
LastEditTime: 2024-01-04 18:30:13
FilePath: \洛谷\【入门1】顺序结构\【深基2.习2】三角形面积.py
Description: 
'''
a,b,c = map(float,input().split())
p = 0.5 * (a+b+c)
result = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print('%.1f' % result)
