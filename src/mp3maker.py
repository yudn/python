
#!/usr/bin/python3
#coding = UFT-8
# import pyttsx3

# #打开文件
# fd = open("C:/Users/admin/code/jiedanle.txt","r",encoding='utf-8')
# #启动阅读器
# engine = pyttsx3.init()
# # engine.setProperty('rate', 150)
# # engine.setProperty('volume', 1)
# #voices = engine.getProperty('voices')
# # print(voices)
# engine.setProperty('voice', engine.getProperty('voices')[0].id)
# lines1=fd.read()
# engine.say(lines1)    
# engine.save_to_file(lines1 , 'bbb.mp3')
# engine.runAndWait()

# # engine = pyttsx3.init()
# # lines=fd.readlines()
# # for line in lines:
# #     engine.say(line)
# #     print(line)
# #     engine.runAndWait()

import pyttsx3
engine = pyttsx3.init()
#engine.setProperty('voice', engine.getProperty('voices')[0].id)
engine.say('hello world')
engine.say('机器学习，深度学习，区块链技术')
engine.runAndWait()
# 朗读一次
engine.endLoop()
 
 
 
 
text='机器学习，深度学习，区块链技术'
Txt2Voice(text)