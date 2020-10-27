#!/usr/bin/python
# -*- coding: UTF-8 -*-
#控制台打印V字符拼接的V
def fun(n):
    s = ''
    for i in range(n):
        tmp = [' '] * (2*n-1)
        j = 2*n-2-i
        if j == i:
            tmp[i] = 'v'
            s += ''.join(tmp).rstrip() + '\n'
            break
        tmp[i] = 'v'
        tmp[j] = 'v'
        s += ''.join(tmp).rstrip() + '\n'
        j -= 1
    return s

print(fun(3))