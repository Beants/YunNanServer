#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/13 10:08 AM
# @Author : maxu
# @Site : 
# @File : getdata.py
# @Software: PyCharm
import re

import bs4
import requests

type_ = 0
result = []
for i in range(10):
    url = 'http://www.ynich.cn/ml?cat_id=11110&type=' + str(type_) + '&batch=-1&city=-1'
    type_ += 1
    # print(url)
    html = requests.get(url).text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    res = soup.find(class_='mllist').__str__()
    # print(res)
    pattern = re.compile('<a href="(.*?)" target="_blank"><img alt="(.*?)" height="180" src="(.*?)" width="200"/>',
                         re.S)
    res = re.findall(pattern, res)
    for i in res:
        result.append([type_, 'http://www.ynich.cn/' + i[0], i[1], 'http://www.ynich.cn/' + i[2]])

rrrr = []
for i in result:
    info = bs4.BeautifulSoup(requests.get(i[1]).text).find(class_='viewc').text
    temp = [i[0], i[2], i[3], info, info]
    rrrr.append(temp)
    print(temp)

from sql import *

temp = SQL()
for i in rrrr:
    temp.new_info(i[0], i[1], i[2], i[3], i[4])
