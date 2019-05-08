#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/8 5:04 PM
# @Author : maxu
# @Site : 
# @File : init.py
# @Software: PyCharm
from flask import Flask, request, jsonify

from sql import SQL

app = Flask(__name__)
sqlManager = SQL()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/login', methods=['POST'])
def login():
    '''
    登录成功 {"type": "login", "_id": temp["_id"]}
    密码错误 0
    查不到用户名则自动注册 {"type": "reg", "_id": temp}
    :return:
    '''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        res = sqlManager.login(username, password)
        return jsonify(res)


@app.route('/star', methods=['POST'])
def star():
    if request.method == 'POST':
        info_id = request.form['info_id']
        user_id = request.form['user_id']
        res = sqlManager.star(info_id, user_id)
        return jsonify(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
