import time

import requests
from bs4 import BeautifulSoup


def main():

  # 搜索的url

    #url = 'https://cn.bing.com/search?q=site%3Aqq.com&qs=n&form=QBRE&sp=-1&pq=site%3Aqq.com&sc=1-11&sk=&cvid=2845944B174F4BEF8D3F8830D22C5892'
    url = 'https://cn.bing.com/search?q=site%3Abaidu.com&qs=n&form=QBRE&sp=-1&pq=site%3Abaidu.com&sc=0-14&sk=&cvid=7A2A299864EC48A6AB007B0C4D9EF362'
    # 打开文件

    file = open('my.txt', 'wb')

    headers = {

        'User-Agent': 'ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400 QQBrowser/9.7.12661.400',

        'Host': 'global.bing.com',

        'Referer': 'http://global.bing.com/?FORM=HPCNEN&setmkt=en-us&setlang=en-us',

        'Upgrade-Insecure-Requests': '1',

        'Cache-Control': 'max-age=0',

        'Connection': 'keep-alive',

        'Cookie': 'DUP=Q=xa-EfMBM4gI7W690UHSTmQ2&T=312971513&A=2&IG=5161BB1CD80C4B8F8E04213C9A6BB2F1; MUID=35B121D519D96CA802AF2AE41DD96FD2; SRCHD=AF=HPCNEN; SRCHUID=V=2&GUID=59BB79AC0CDE4D8F853C004286CA05C4&dmnchg=1; SRCHUSR=DOB=20171201; MUIDB=35B121D519D96CA802AF2AE41DD96FD2; ULC=H=1D535|1:1&T=1D535|1:1; _RwBf=s=70&o=16; ipv6=hit=1512120707130&t=4; _EDGE_S=mkt=en-us&ui=en-us&SID=0AC562F3333D612722A469B832E160FE; SNRHOP=I=&TS=; _SS=SID=0AC562F3333D612722A469B832E160FE&HV=1512117115&R=0&bIm=473689; SRCHHPGUSR=CW=654&CH=997&DPR=1&UTC=480&WTS=63647713897'

    }

# 设置爬虫页数

    for i in range(1, 5):

        data = {

            'q': 'site:baidu.com',

            'qs': 'n',

            'sp': '3',

            'sc': '0-12',

            'sk': '',

            'cvid': '7A2A299864EC48A6AB007B0C4D9EF362',

            'first': i*12,

            'FORM': 'PERE'

        }

        # 构建会话

        sessions = requests.Session()

# 模拟浏览器请求数据

        results = sessions.get(url, headers=headers, params=data)

        soup = BeautifulSoup(results.content, 'html.parser')

        # 获取关键性信息

        job_bt = soup.findAll('h2')

        # 把信息写入文件

        for i in job_bt:

            print(i.a.get('href'))

            file.write((i.a.get('href')).encode('utf-8')+'\n'.encode('utf-8'))

        # 进入休眠，避免网站识别为频繁访问而获取信息失败

        time.sleep(3)

    # 关闭文件

    file.close()


if __name__ == '__main__':

    main()
