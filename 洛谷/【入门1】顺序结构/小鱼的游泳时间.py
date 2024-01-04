'''
Author: PuPu 877770086@qq.com
Date: 2024-01-04 20:15:34
LastEditors: PuPu 877770086@qq.com
LastEditTime: 2024-01-04 20:20:44
FilePath: \洛谷\【入门1】顺序结构\小鱼的游泳时间.py
Description: 
'''
a,b,c,d = map(int,input().split())
t = c * 60 + d - a * 60 - b
print(t//60,t%60)
print(divmod(t,60))