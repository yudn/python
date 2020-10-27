#!/usr/bin/python3
import os

def main():
    filename = input("请输入文件名:")
    if os.path.exists(filename):
        content=""
        try:
            f = open(filename, "r")
            content = f.read()
            f.close()
            change_content = content.swapcase()
            print(change_content)
        except Exception as ret:
            print('读取文件出错，没有这个文件！', ret)
    

if __name__ == "__main__":
    main()


