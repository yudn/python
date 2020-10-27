# -*-coding: UTF_8-*-
#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import os
import time

# 程序运行开始提示
print("程序于 {} 开始启动，请等待...".format(time.ctime()))
# 美女图片类型和对应的页面序列位置，图片类型为键，位置为 值
# 这个位置用于图集的链接，如list_6_3.html，6即为性感美女的序列位置
girls_images_type = {'xinggan': '6', 'qingchun': '1',
                     'xiaohua': '2', 'chemo': '3', 'qipao': '4', 'mingxing': '5'}

# 创建soup对象


def creat_soup(url):
    '''
    该函数返回一个url的soup对象
    :param url:一个页面的链接
    '''
    # 获取网页，得到一个response对象
    response = requests.get(url)
    # 指定自定义编码，让文本按指定的编码进行解码，因为网站的charset = gb2312
    response.encoding = 'gb2312'
    # 使用解码后的数据创建一个soup对象，指定HTML解析器为Python默认的html.parser
    return BeautifulSoup(response.text, 'html.parser')


def pages_url(image_type, position):
    '''
    该函数用于获取某一个图片类型的全部页面的链接
    :param image_type:美女图片的类型，只有6种，是一个列表
    '''
    url = 'http://www.mm131.net/' + image_type
    # 调用函数，创建soup对象
    soup = creat_soup(url)
    # 查找当前图片类型的分页链接
    images_information = soup.find(class_="page").find_all('a')
    # 计算当前图片类型共有多少页
    # 先获取最后一个a标签，格式是 list_1_31.html
    # 然后将该字符串里面的'.' 替换为 '_'，最后再使用split分割字符串，得到一个列表
    pages_num_list = images_information[-1].get(
        'href').replace('.', '_').split('_')
    # 当前图片类型共有多少页
    pages_num = int(pages_num_list[-2])

    # 用于存储每一页的页面链接，默认存储第一页的页面链接
    pages_url = [url]
    # 将当前图片类型的每一页的链接存储起来，从第二页开始链接后跟list_position_页码.html
    for page in range(2, pages_num + 1):
        pages_url.append(url + '/list_' + position + '_' + str(page) + '.html')

    # 函数返回某一个图片类型的全部页面链接
    return pages_url


def atlas(pages_url):
    '''
    该函数用于存储某一个页面的所有图集链接
    :param pages_url:页面链接，可以是列表
    '''
    # 用于存储每一个图集链接的列表
    atlas_url = []
    for page_url in pages_url:
        # 调用函数，创建页面链接的soup对象
        soup = creat_soup(page_url)
        # 查找当前页面所有的图集信息，find_all 返回的是一个列表
        atlas_information = soup.find(
            class_="list-left public-box").find_all('dd')
        for information in atlas_information:
            # 排除page 分页的链接
            if not information.find('span'):
                # 将符合条件的链接，即 每一个图集的链接加入到列表中
                atlas_url.append(information.find('a').get('href'))
    # 函数返回某一个页面的全部图集链接
    return atlas_url


def save_images(atlas_url):
    '''
    该函数用于将某一图集的所有图片保存下来
    :param atlas_url:图集链接，可以是个列表
    '''
    # 共有多少个图集
    length = len(atlas_url)
    # 已下载图集
    count = 1
    for url in atlas_url:
        # 调用函数，创建图集链接的soup对象
        soup = creat_soup(url)
        # 指定文件夹名
        file_folder = soup.find(class_='content').h5.string
        # 将图片文件夹保存在程序文件所在目录的imgase目录下
        folder = 'images/' + file_folder + '/'
        if os.path.exists(folder) == False:  # 判断文件夹是否存在
            os.makedirs(folder)  # 创建文件夹
        # 当前图集 共多少张图片,span的内容结构是共XX页，XX为当前图片的张数
        images_number = int(soup.find('span', class_='page-ch').string[1:-1])
        # 当前图集的编号，如图集链接 http://www.mm131.net/qingchun/3039.html，编号为3039，用于拼接当前图集的图片地址
        pic_number = url.replace('.', '/').split('/')[-2]
        # 创建列表，用于保存每一张图片的链接
        images_url = []
        for number in range(1, images_number+1):
            images_url.append('https://img1.nthjjz.com/pic/' +
                              pic_number + '/' + str(number) + '.jpg')
        # 有些网站会有防盗链，原理是检查 HTTP的referer头，如果没有referer，会抓取不了数据
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36',
                   'referer': "http://www.mm131.net/xinggan/530.html"}
        # 开始下载提示，等待2秒后开始下载
        print("开始下载图集 {}，剩余图集 {}".format(file_folder, length - count))
        time.sleep(2)
        for index, image_url in enumerate(images_url):
            # get函数发送图片链接访问请求
            html = requests.get(image_url, headers=headers)
            # 保存图片至指定的文件夹，并将文件进行命名
            image_name = folder + str(index + 1) + '.jpg'
            # 以byte形式将图片数据写入
            with open(image_name, 'wb') as file:
                file.write(html.content)
            print('第{}张图片下载完成,开始下载第{}张图片...'.format(index+1, index+2))
        # 已下载图集加1
        count += 1
    print("当前图集图片已下载完成\n")


# 获取某一图片类型的所有页面链接，可以使用循环遍历字典 girls_images_type，获取所有的图片类型的所有页面链接，
# 那样运行时间太长，这里为了演示，只取其中一个图片类型
# 性感美女 和 清纯美眉 是最养眼的，不用谢~~
pages_url = pages_url('qingchun', '1')

# 获取页面的所有图集链接
atlas_url = atlas(pages_url)

# 下载图集的图片
save_images(atlas_url)
