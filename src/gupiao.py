# -*-coding: UTF_8-*-
#!/usr/bin/python
import requests
import csv
url = 'https://xueqiu.com/hq'


def getHtmlList(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/51.0.2704.63 Safari/537.36'}
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        data = r.json()

        data_list = data['data']['list']
        for i in data_list:
            dit = {}
            dit['股票代码'] = i['symbol']
            dit['股票名字'] = i['name']
            dit['当前价'] = i['current']
            dit['涨跌额'] = i['chg']
            dit['涨跌幅/%'] = i['percent']
            dit['年初至今/%'] = i['current_year_percent']
            dit['成交量'] = i['volume']
            dit['成交额'] = i['amount']
            dit['换手率/%'] = i['turnover_rate']
            dit['市盈率TTM'] = i['pe_ttm']
            dit['股息率/%'] = i['dividend_yield']
            dit['市值'] = i['market_capital']
            print(dit)
        f = open('股票数据.csv', mode='a', encoding='utf-8-sig', newline='')
        csv_writer = csv.DictWriter(f, fieldnames=[
                                    '股票代码', '股票名字', '当前价', '涨跌额', '涨跌幅/%', '年初至今/%', '成交量', '成交额', '换手率/%', '市盈率TTM', '股息率/%', '市值'])
        csv_writer.writeheader()
        csv_writer.writerow(dit)
        f.close()

    except:
        print("err:")
