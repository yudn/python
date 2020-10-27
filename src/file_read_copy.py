#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import shutil


def main():
    # 当前目录下的文件
    file_path = 'test1.sh'
    if os.path.exists(file_path):
        content = ""
        with open(file_path, 'r') as f:
            content = f.read()
        change_content = content.swapcase()
        print(change_content)
    else:
        print("路径出现错误，无法打开指定文件")
# 复制文件  常用于拷贝数据库文件


def copyfile():
    shutil.copyfile('1.txt', '2.txt')
    if os.path.exists('2.txt'):
        print('copy success')


if __name__ == "__main__":
    main()
    copyfile()
