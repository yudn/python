import os
import random

file = 'C:\\Users\\mac\\Pictures\\left'
j=0
for i in os.listdir(file):
    if (i.endswith('.jfif')):
        j = j+1
        y=""
        for x in range(16):
            index=random.randrange(0,10)  #生成一个0~10位的数z
            if index!=x and index +1 !=x:
                    y +=chr(random.randint(97,122))  # 生成a~z中的一个小写字母
            elif index +1==x:
                    y +=chr(random.randint(65,90) ) # 生成A~Z中的一个大写字母
            else:
                    y +=str(random.randint(1,9))  # 数字1-9
        new_name = 'left' + y + '.jpg'
        os.chdir(file)  #没有这一步的话会报 FileNotFoundError  的错误
        os.rename(i, new_name)
        print(i)
    else:        
        print("no")

    