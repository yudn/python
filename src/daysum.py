a = 0
file = input('请输入要计算的文件名称')
#f = open("C:/Users/mac/Desktop/20101216-sum.txt", "r", encoding="utf-8")

f = open(file, "r", encoding="utf-8")
anums = f.readlines()
for line in anums:
    d = a + int(line)
    #单位转换为GB

    u = d/1024/1024/1024

print(d)    

print("今天注入" + str(u) + "TB")    


