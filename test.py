#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/8 11:52 PM
# @Author : maxu
# @Site : 
# @File : test.py
# @Software: PyCharm
import requests


# 测试登录注册
# data = {'username': 'admin', 'password': 'admin'}
# res = requests.post('http://39.96.222.175:5000/login', data=data)
# print(res.text)
# print(type(res))

# 测试star
# data = {'user_id': '5cd2a251f9c23996741bdb12', 'info_id': '5cd30e712fa5d21df8d2f7ed'}
# # res = requests.post('http://127.0.0.1:5000/star', data=data)
# # print(res.text)
# # print(type(res))

# # 测试获取info——like
# data = {'user_id': '5ce193e3c9a49cb81b562fe7'}
# res = requests.post('http://39.96.222.175:5000/get_users_like', data=data)
# print(res.text)
# print(type(res))

# 测试get info

# data = {'user_id': '5cd2fc24757ae06cb0f94ed7', 'info_id': '5cd30e712fa5d21df8d2f7ed'}
# res = requests.post('http://39.96.222.175:5000/get_info_all', data=data)
# print(res.text)
# print(type(res))

# 测试get info
# data = {'user_id': '5cd2a251f9c23996741bdb12', 'info_id': '5cd30e712fa5d21df8d2f7ed'}
# res = requests.post('http://127.0.0.1:5000/get_info_one', data=data)
# print(res.text)
# print(type(res))
#5ce193e3c9a49cb81b562fe7

# 测试get key
data = {'type': 1}
res = requests.post('http://127.0.0.1:5000/get_info_type', data=data)
print(res.text)
# print(type(res))
