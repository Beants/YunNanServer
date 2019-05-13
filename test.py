#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/8 11:52 PM
# @Author : maxu
# @Site : 
# @File : test.py
# @Software: PyCharm


# 测试登录注册
# data = {'username': 'user1', 'password': 'user1'}
# res = requests.post('http://127.0.0.1:5000/login', data=data)
# print(res.text)
# print(type(res))

# 测试star
# data = {'user_id': '5cd2a251f9c23996741bdb12', 'info_id': '5cd30e712fa5d21df8d2f7ed'}
# # res = requests.post('http://127.0.0.1:5000/star', data=data)
# # print(res.text)
# # print(type(res))

# # 测试获取info——like
# data = {'user_id': '5cd2a251f9c23996741bdb12'}
# res = requests.post('http://127.0.0.1:5000/get_users_like', data=data)
# print(res.text)
# print(type(res))

# 测试get info
import requests

data = {'user_id': '5cd2fc24757ae06cb0f94ed7', 'info_id': '5cd30e712fa5d21df8d2f7ed'}
res = requests.post('http://39.96.222.175:5000/get_info_all', data=data)
print(res.text)
print(type(res))

# 测试get info
# data = {'user_id': '5cd2a251f9c23996741bdb12', 'info_id': '5cd30e712fa5d21df8d2f7ed'}
# res = requests.post('http://127.0.0.1:5000/get_info_one', data=data)
# print(res.text)
# print(type(res))
