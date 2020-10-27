#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
#求两个list的交集
def jiaoji():
    nums1 = [1, 2, 2, 2, 1]
    nums2 = [2, 2, 2]
    tmp = [val for val in nums1 if val in nums2]
    print("交集为", tmp)
#升序排序
def sort():
    aList = [6, 4, -3, 5, -2, -1, 0, 1, -9]
    aList.sort(reverse=True)
    print( 'alist:', aList)
#单词字典排序
def zdx(sword):
    l = []
    temp = sword.split(" ")
    for i in temp:
        if i.lower() not in [j.lower() for j in l]:
            l.append(i)
    return " ".join(sorted(l, key=str.lower))

while True:
    s = input("请输入用空格进行分隔的单词：")
    if len(s) <= 255:
        p = re.compile(r"^[a-zA-Z\s]{0,255}$")  
        if p.match(s):
            print("输入合格：" + s)
            test = zdx(s)
            print("按字典序排列输出为：%s" % test)
            break
        else:
            print("输入只能是字母或空格，请重新输入!")
    else:
        print("输入不得超过255个字符，请重新输入!")
#调用函数
def main():
    zdx(s)
    jiaoji()
    sort()
#函数入口    
if __name__ == "__main__":
    main()
