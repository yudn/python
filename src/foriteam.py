#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 1:for 循环遍历
# list 循环
words = ['cat', 'window', 'defens']
for i in range(len(words)):
    print('a=', words[i])
# 散列
woods = {'cat', 'window', 'defens'}
for j in woods:
    print('b=', j)
# 表输出使用iteams()
table = {'Soerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# 矩阵转置一次，发生90度偏移
a = [[row[i] for row in matrix] for i in range(4)]
print(a)
b = [[row[i] for row in a] for i in range(4)]
print(b)
