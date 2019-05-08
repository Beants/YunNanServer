#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/8 11:52 PM
# @Author : maxu
# @Site : 
# @File : test.py
# @Software: PyCharm


import requests

data = {'username': 'user1', 'password': 'user1'}
res = requests.post('http://127.0.0.1:5000/login', data=data)
print(res.text)
print(type(res))
