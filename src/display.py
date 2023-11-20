import os
import glob
from Pillow import Image
from tkinter import Tk, Label

# 指定图片文件夹路径
#image_folder = '路径/到/你的/图片文件夹'
image_folder ='C://Users//admin//Pictures'

# 获取文件夹中的所有图片文件
image_files = glob.glob(os.path.join(image_folder, '*.jpg')) + glob.glob(os.path.join(image_folder, '*.png'))

# 创建Tkinter窗口
window = Tk()
window.title("图片播放器")

# 创建Label组件用于显示图片
image_label = Label(window)
image_label.pack()

# 定义函数切换并显示下一张图片
def show_next_image(index):
    # 若已经显示完所有图片，则重新开始播放
    if index >= len(image_files):
        index = 0
    
    # 加载并显示图片
    image_path = image_files[index]
    image = Image.open(image_path)
    image_label.configure(image=image)
    image_label.image = image
    
    # 延迟一段时间后继续播放下一张图片
    window.after(2000, lambda: show_next_image(index + 1))

# 开始播放图片
show_next_image(0)

# 运行Tkinter事件循环
window.mainloop()
