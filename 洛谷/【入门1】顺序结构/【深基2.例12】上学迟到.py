'''
Author: PuPu 877770086@qq.com
Date: 2024-01-04 19:29:41
LastEditors: PuPu 877770086@qq.com
LastEditTime: 2024-01-04 20:09:06
FilePath: \洛谷\【入门1】顺序结构\【深基2.例12】上学迟到.py
Description: 
'''
s,v =map(int,input().split())

if s % v !=0:
    tmp = int(s / v) + 1
else:
    tmp = int(s / v)
t = (32 * 60 - tmp - 10) % 1440
a,b = map(int,divmod(t, 60))
print('%02d:%02d'%(a,b))
