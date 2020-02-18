# -*- coding: utf-8 -*-

import requests
import json

# 爬取json内容例子，爬取豆瓣图片并本地存储
def download(src, id):
    dir = './' + str(id) + '.jpg'
    try:
        pic = requests.get(src, timeout = 10)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except Exception as ex:
        print(ex)

for i in range(0, 22471, 20):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    query = '王祖贤'
    url = 'https://www.douban.com/j/search_photo?q='+query+'&limit=20&start=' + str(i)
    html = requests.get(url, headers=headers)
    response = json.loads(html.text, strict=False)

    #下载对应图片
    for image in response['images']:
        print(image['src'])
        download(image['src'], image['id'])
