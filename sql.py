#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/8 5:04 PM
# @Author : maxu
# @Site : 
# @File : sql.py
# @Software: PyCharm
from bson import ObjectId


class SQL:
    def __init__(self):

        import pymongo

        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["Yunnan"]

    def login(self, username, password):
        table = self.mydb['user']
        temp = table.find_one({"username": username})
        if temp:
            if temp['password'] == password:
                return {"type": "login", "data": str(temp["_id"])}
            else:
                return {"type": "login", "data": "password error"}
        else:
            temp = self.reg(username, password)
            return {"type": "reg", "data": str(temp)}

    def reg(self, username, password):
        table = self.mydb['user']
        mydict = {"username": username, "password": password}
        if not table.find_one({"username": username}):
            x = table.insert_one(mydict)
            return x.inserted_id
        else:
            return '0'

    def new_info(self, type_, image, title, info, detail):
        table = self.mydb['info']
        mydict = {"image": image, 'title': title, "info": info, "type": type_, "detail": detail, 'star': []}
        x = table.insert_one(mydict)
        return x.inserted_id

    def get_info_all(self):
        table = self.mydb['info']
        res = []
        for i in table.find({}):
            temp = str(i['_id']).replace('ObjectId(', '').replace(')', '')
            i['_id'] = temp
            res.append(i)
        res = {
            "type": "get_info_all",
            "res": res
        }
        print(res)
        return res

    def get_info_like(self, user_id_):
        table = self.mydb['info']
        user_id = ObjectId(user_id_)
        res = []
        for item in self.get_info_all()["res"]:
            if user_id_ in item['star']:
                res.append(item)
        res = {
            "type": "get_users_like",
            "user": user_id_,
            "res": res
        }
        print(res)
        return res

    def get_info_type(self, type_):
        table = self.mydb['info']
        res = []

        for item in table.find({"type": type_}):
            temp = str(item['_id']).replace('ObjectId(', '').replace(')', '')
            item['_id'] = temp
            res.append(item)
        res = {
            "type": "get_users_type",
            "res": res
        }
        # print(res)
        return res

    def get_info_one(self, info_id_, user_id_):

        info_id = ObjectId(info_id_)

        user_id = ObjectId(user_id_)
        table = self.mydb['info']
        temp = table.find_one({'_id': info_id})
        print('get_info', temp)
        star = 0
        print(temp)
        if user_id_ in temp['star']:
            star = 1
        return {
            "_id": info_id_,
            "image": temp['image'],
            "title": temp['title'],
            "info": temp['info'],
            "detail": temp['detail'],
            "type": temp['type_'],
            "star": star
        }

    def star(self, info_id_, user_id_):

        info_id = ObjectId(info_id_)

        table = self.mydb['info']
        temp = table.find_one({'_id': info_id})
        print('atar', temp['star'])
        temp = list(temp['star'])
        if user_id_ in temp:
            temp.remove(user_id_)
            print(temp)
            f = table.update_one({'_id': info_id}, {'$set': {'star': temp}})
            return {"type": "star", "state": "0"}
        else:
            temp.append(user_id_)
            print(temp)
            f = table.update_one({'_id': info_id}, {'$set': {'star': temp}})
            return {"type": "star", "state": "1"}

    def search_by_key(self, title):
        table = self.mydb['info']

        res = []
        for i in table.find({}):
            if title in i['title'] or i in i['info'] or i in i['detail']:
                temp = str(i['_id']).replace('ObjectId(', '').replace(')', '')
                i['_id'] = temp
                res.append(i)

        res = {
            "type": "search_by_key",
            "res": res
        }
        return res




if __name__ == '__main__':
    pass
    temp = SQL()
    temp.get_info_all()
