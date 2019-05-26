#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/8 5:04 PM
# @Author : maxu
# @Site : 
# @File : init.py
# @Software: PyCharm
import codecs
import json
import sys

from flask import Flask, request, Response

from sql import SQL

# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

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
        return Response(json.dumps(res), mimetype='application/json')


@app.route('/star', methods=['POST'])
def star():
    if request.method == 'POST':
        info_id = request.form['info_id']
        user_id = request.form['user_id']
        res = sqlManager.star(info_id, user_id)
        return Response(json.dumps(res), mimetype='application/json')


@app.route('/get_users_like', methods=['POST'])
def get_users_like():
    if request.method == 'POST':
        user_id = request.form['user_id']
        res = sqlManager.get_info_like(user_id)
        print(res)
        return Response(json.dumps(res), mimetype='application/json')


@app.route('/get_info_all', methods=['POST'])
def get_info_all():
    if request.method == 'POST':
        res = sqlManager.get_info_all()
        print(res)
        return Response(json.dumps(res), mimetype='application/json')


@app.route('/get_info_one', methods=['POST'])
def get_info_one():
    if request.method == 'POST':
        info_id = request.form['info_id']
        user_id = request.form['user_id']

        res = sqlManager.get_info_one(info_id, user_id)
        print(res)
        return Response(json.dumps(res), mimetype='application/json')


@app.route('/get_info_type', methods=['POST'])
def get_info_type():
    if request.method == 'POST':
        type_ = request.form['type']

        res = sqlManager.get_info_type(type_)
        print(res)
        return Response(json.dumps(res), mimetype='application/json')


@app.route('/get_info_key', methods=['POST'])
def get_info_key():
    if request.method == 'POST':
        key = request.form['key']
        print(key)
        res = sqlManager.search_by_key(key)
        print(res)
        return Response(json.dumps(res), mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # print(get_info_all())
