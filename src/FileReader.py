#!/usr/bin/python3
#coding = UFT-8
import pyttsx3
#打开文件
fd = open("C:/Users/admin/code/python/src/threeKingdoms.txt","r",encoding='utf-8')
#启动阅读器
engine = pyttsx3.init()
lines1=fd.read()
engine.say(lines1)    
#engine.save_to_file(lines1 , 'bbb.mp3')
engine.runAndWait()

engine = pyttsx3.init()
lines=fd.readlines()
for line in lines:
    engine.say(line)
    print(line)
    engine.runAndWait()


