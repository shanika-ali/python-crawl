# -*- coding: utf-8 -*-

# etree xpath解析dom树时
import requests
from selenium import webdriver
import xlwt
from lxml import etree

# 爬取html页面元素，爬取豆瓣最新图书的名字和评分，导入excel
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'https://book.douban.com/latest?icn=index-latestbook-all'
driver = webdriver.Chrome()
driver.get(url)
html = etree.HTML(driver.page_source)

score_xpath = '//*[@id="content"]/div/div[2]/ul//div/p[1]/span[2]'
title_path = '//*[@id="content"]/div/div[2]/ul//div/h2/a'

workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')
style = xlwt.XFStyle() # 初始化样式
font = xlwt.Font() # 为样式创建字体
font.bold = True # 黑体
style.font = font # 设定样式
worksheet.write(0, 0, '书名', style) # 不带样式的写入
worksheet.write(0, 1, '评分', style) # 带样式的写入

scores = html.xpath(score_xpath)
titles = html.xpath(title_path)

i = 1
for score, title in zip(scores, titles):
    print(score.text)
    worksheet.write(i, 0, str(title.text))
    worksheet.write(i, 1, score.text)
    i += 1

workbook.save('douban_book.xls')


