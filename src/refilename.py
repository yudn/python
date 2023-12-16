# -*- coding: utf-8 -*-

import os
def refilename(filepath,renames_list):
    """批量修改文件名（列表中名字个数要和原文件个数相等）

    :param filepath: 所有文件所在的文件夹路径（第一个参数）
    :param renames_list: 要修改的名字所成的列表（第二个参数）
    :return: 1表示结束
    """
    name_list = os.listdir(filepath)    # 将文件夹下的所有文件的名字放入一个列表
    if filepath[-1] != '/':             # 判断用户输入的文件夹的路径是否在最后加上/
        filename = filepath + '/'       # 给没有加/的加上/
    else:
        filename = filepath              # 已经加上的就不再加/
    houzhui = name_list[0][name_list[0].find('.'):]   # 找到文件后缀
    for i in range(len(name_list)):
        name = name_list[i]
        rename = renames_list[i]
        os.rename(filename+name,filename+rename+houzhui) # os的rename方法第一个参数是文件的原名字，第二个是新名字
    return 1             # 表示执行结束

def main():
    name_list = [f'{i}' for i in range(1,101)]   # 用列表生成式生成一个包含新名字列表
    print(refilename('d:\\共鸣高能学院\\9、国学殿堂\\道学精要\\道德经\\道德经配图',name_list))

if __name__ == '__main__':
    main()
