from PIL import Image, ImageDraw, ImageFont
'''
图片修改大小，创建插入文字,拼接图片
'''
# 打开图片文件
im = Image.open("D:\\共鸣高能学院\\9、国学殿堂\\道学精要\\道德经\\道德经配图\\3.jpg")

# 设置新的图片尺寸
width = 400
height = 400

# 调整图片尺寸
im_resized = im.resize((width, height))

# 保存新的图片文件
im_resized.save("D:\\共鸣高能学院\\9、国学殿堂\\道学精要\\道德经\\道德经配图\\3.jpg")


# ##创建一个空拜图片，写几个字
# img = Image.new('RGB', (500, 500), color='white')
# img.save('C:\\Users\\admin\\Pictures\\example.png')
# # 打开图片
# image = Image.open('C:\\Users\\admin\\Pictures\\example.png')

# # 创建一个Draw对象
# draw = ImageDraw.Draw(image)

# # 设置字体和字号
# font = ImageFont.truetype('arial.ttf', 36)

# # 添加文字
# draw.text((50, 50), 'Hello, World!', font=font, fill=(120, 0, 60))

# # 保存图片
# image.save('C:\\Users\\admin\\Pictures\\new_image.png')



# #两张图片拼接在一起

# # # 打开两张图片
# image1 = Image.open('D:\\共鸣高能学院\\9、国学殿堂\\道学精要\\道德经\\道德经配图\\1.jpg')
# image2 = Image.open('D:\\共鸣高能学院\\9、国学殿堂\\道学精要\\道德经\\道德经章节图片\\1.png')

# # 获取两张图片的大小
# width1, height1 = image1.size
# width2, height2 = image2.size

# # 创建一张新的图片，大小为两张图片的宽度之和和高度中的较大值
# new_image = Image.new('RGB', (width1 + width2, max(height1, height2)))

# # 将第一张图片粘贴到新图片的左侧
# new_image.paste(image1, (0, 0))

# # 将第二张图片粘贴到新图片的右侧
# new_image.paste(image2, (width1, 0))

# # 保存新图片
# new_image.save('D:\\共鸣高能学院\\9、国学殿堂\\道学精要\\道德经\\ddj-1.jpg')

