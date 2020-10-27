#!/usr/bin/python
# -*- coding: UTF-8 -*-
#嵌套法格式化输入数据
a,b=input().split(';')
c,d,e=map(float, b.split(','))
print('The each subject score of no.={},C语言={} ，数学={},英语={}'.format(int(a),float(c),float(d),float(e)))

#输入1行输出1个金字塔
a=input()
for i in range(5):
    print(" "*(4-i) + (a+' ')*(i+1) )