# -*-coding: UTF_8-*-
#!/usr/bin/python
'''
    对输入的数据交换位置，或者更具不统情况转换数据
    a 和 b 交换位置
'''
a, b = input().split(",")
a_num = a[:]
b_num = b[:]
a_num, b_num = b_num, a_num
print("a={},b={}".format(a_num, b_num))