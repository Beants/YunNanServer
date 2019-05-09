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

    def search_by_title(self, title):
        table = self.mydb['info']

        res = []
        for i in table.find({}):
            if title in i['title'] or i in i['info'] or i in i['detail']:
                temp = str(i['_id']).replace('ObjectId(', '').replace(')', '')
                i['_id'] = temp
                res.append(i)

        res = {
            "type": "search_by_title",
            "res": res
        }
        return res




if __name__ == '__main__':
    temp = SQL()
    # print(temp.reg('admin', 'admin'))
    # print(temp.login('admin', 'admin'))
    # print(temp.new_info('food',
    #                     'https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=78c401b9afc27d1eb12b33967abcc60b/21a4462309f7905234d9f42307f3d7ca7acbd5ed.jpg',
    #                     '云南菜', '滇菜即云南菜，是中国菜体系中民族特色最为突出的一个地方性菜系。',
    #                     "## 特色菜点：\n" +
    #
    #                     "* 以昆明、楚雄、玉溪为中心的滇中地区历来是云南省政治、经济、文化和交通的中心，这里气候温和，雨量充沛，自然资源丰富，名厨多汇，兼收历代地方、民族饮食之精华，云南饮食文化的多样性、复杂性、融合性等特点在这一地区表现的尤为突出和鲜明。滇中地区的饮食兼收并蓄，体现多种文化的交流，新的饮食风尚和饮食观念推动和左右着云南滇菜文化的潮流，同时也成为反映云南饮食文化变迁的主要窗口，是云南滇菜的精华代表。\n" +
    #
    #                     "* 以曲靖、宣威、昭通为中心的滇东北地区曾是南方丝绸之路入滇的必经之地，因接近内地，交通较为便利，与中原交往较多。两千多年前就接受了四川地区经济与文化的影响，其饮食文化具有云南地方汉族与当地少数民族( 如彝族) 文化交融的特点，菜肴烹调方法、口味与川菜相似。以丽江、中甸为中心的滇西北区位于青藏高原的南端，气候偏凉，畜牧业发达。丽江、中甸曾是唐代开通的由大理至拉萨道路的必经之地，即“茶马古道”，为马帮文化的交通枢纽。因此，滇西北区的饮食文化具有鲜明的高原民族特色与地方特色，高能量食物如青稞、各种面饼、牛羊肉、自酿粮食酒与砖茶，构成当地饮食主体。\n" +
    #
    #                     "* 以大理为中心的滇西区表现出浓郁的白族饮食文化特色，较多地保留了南诏、大理国古老的饮食传统，当地盛产的乳制品、淡水湖的水产品、梅子、地方酿造酒、本地茶叶等使滇西区的菜点具有鲜明的地方与民族特色。\n![](https://gss2.bdstatic.com/-fo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike92%2C5%2C5%2C92%2C30/sign=5619626aae4bd11310c0bf603bc6cf6a/242dd42a2834349b9db7e89ccaea15ce36d3be72.jpg)" +
    #
    #                     "* 以德宏、临沧、版纳为中心的滇南区为外地汉族移民与当地少数民族( 傣族、景颇族等) 、东南亚地区诸饮食文化的结合体，同时又具有鲜明的热带、亚热带饮食文化的特点，明显地反映出傣族等稻作民族的饮食传统。由于当地土地肥沃，盛产各类植物和花卉，以可食的野生菌类、野菜、水果与花卉、昆虫入席，发酵食品多，烹饪加工方式古朴，蘸料口味独特，糯米为主食等是当地饮食特色。" +
    #                     "\n\n## 特色特点\n" +
    #                     "* 丰富的生态原材料\n" +
    #                     "云南地处云贵高原，山脉绵延，平坝与湖泊镶嵌其间，形成绮丽多姿的风光景色和热带、亚热带、温带和寒带的立体气候类型，这种多样的地貌与气候极其有利于多种动植物的生长，使滇菜取材用料广泛、丰富而又独特，并且大部分来自天然，具有绿色、营养、生态、保健的特点。云南被誉为“菌类王国”、“植物王国”和“动物王国”，是中国乃至世界食用野生菌资源最丰富的地区之一，有250余种可食用野生菌，常见的有牛肝菌、青头菌、鸡枞、干巴菌、竹荪、松茸等。 \n" +
    #                     "在四季如春的云南，鲜花不仅是观赏的植物，而且还是餐桌上的佳肴，许多名贵的花卉如菊花、白杜鹃花、玫瑰花、百合、玉兰、桂花等均可制成上乘的鲜花名菜名点。云南出产的珍贵药材如三七、虫草、天麻等是上佳的滋补药材。云南常年蔬菜不断青，山茅野菜遍地可寻，有春食花、夏食菌、秋食果、冬食菜之说，体现出清淡纯朴、原汁原味、鲜嫩回甜的风味; 星罗棋布、大小不一的高原湖泊繁衍着多种鱼、虾、蛙类，使得饮食呈现出用料广泛、物种繁多、乡土气息浓郁的特色，形成了一批深受大众欢迎的云南民间乡土菜和特色菜。尤其是一些特产及特殊调味品的使用，在菜肴风味形成中有很大作用，如宣威火腿、乳饼、香茅草、昭通酱、丘北辣椒、路南卤腐、曲靖韭菜花、玫瑰大头菜等具有鲜明特色的优质酱菜和特色调料，为滇菜带来了独特的口味，为滇菜的发展提供了必要而特殊的物质基础。 \n" +
    #                     "独特的工艺技法\n" +
    #                     "烹调工艺是形成菜肴的重要手段。许多风味菜名传遐迩，在炊具、火功、味形和制法上都有着独特之处 [3]  。云南是一个少数民族大省， 25个少数民族朴实而古老的烹调方法与汉族的烹饪技艺相结合，使得滇菜的工艺技法丰富多彩，既有汉族的蒸、炸、熘、卤、氽、炖，又融合了少数民族的烤、舂、焐、腌、石烹、隔器盐焗等烹食方法，具有浓郁的古风遗韵，反映了云南少数民族的生活习俗。例如: 烤是少数民族肉食烹制的常见之法，但烤的过程又辅之以西双版纳特有的香茅草，烤出了个性化的食俗风味。在工业时代科技进步的情况下，滇菜依然保留着这些当地特有的烹饪诀窍、方式和方法，是非常难得和有意义的。少数民族的饮食器具大都用竹器、陶器、木器、树叶等天然材料，如用香竹装入糯米烤制的竹筒饭软糯清香，用挖空的菠萝制作的菠萝紫米饭带有清香的菠萝味，用建水紫陶特制的汽锅制作的汽锅鸡原汁原味、肉嫩香汤清鲜。这些烹饪技法和饮食器具的选择体现了云南人民适应环境、顺应自然的思想。\n" +
    #                     "* 鲜明的民族特色\n" +
    #                     "云南的25个少数民族，每个民族都有各自独特的传统习俗以及饮食文化，种独特的资源。滇菜在形成过程中，将各少数民族的民族风俗、饮食习惯、烹调方法、独特口味、人文历史和特有的生态资源进行了有机融合和创新，形成了滇菜独有的历史、人文、民族风情和自然特色。这种蕴藏的几千年深厚的历史风貌、民族精神和文化底蕴，已经成为滇菜发展的一大支撑点和闪光点，而且无可替代。因此与其他菜系不同的是，滇菜是具有鲜明的多民族菜系特色、又具有突出地方菜系特点的菜种，其造型、色泽、烹饪方法、香味及滋补功效别具一格，体现在食材丰富、饮食风俗多彩、烹调方法多样、口味独特多变等方面。\n" +
    #                     "* 多格局的乡土筵席\n" +
    #                     "筵席是烹调工艺的集中反映和名菜名点的汇展橱窗，所以具有不同格局、风味各异的乡土筵席，是评判和区分菜系的一项具体指标。早在清朝光绪年间，昆明已形成了“三冷荤、四热吃、四座碗、八小碗、十二围碟”的旧式筵席及“十大件”的新式筵席，风味独特 [5]  。形成了形式多样各具特色的不同种类和档次的滇味筵席，如1999年世博会的开幕国宴———“吉鑫宴舞”，是由筵席与歌舞相组成。其中除了看家菜过桥米线外，还将云南哈尼族的长街宴、傣族的迎亲酒、纳西族三叠水、彝族的砣子肉等都融会于吉鑫宴舞的筵席中。一次吉鑫宴舞，就可以尝遍云南美食，并且将云南多个民族的民族文化和民俗风情都融会于宴舞之中。其他具有民族饮食文化又与现代餐饮时尚相结合的大理白族风情宴、楚雄彝王宴、德宏土司宴、哈尼长街宴、云南山珍宴、鸡枞全席等，都是滇菜中富有浓郁乡土气息的知名筵席。哈尼族长街宴曾到北京摆出千道滇菜，创造了上海吉尼斯纪录，为昆明荣获中国首座“中华美食名城”增添了亮点。"))
    # print(temp.star('5cd3bd685d9b1cfdd763ea63', '5cd2a251f9c23996741bdb12'))
    # print(temp.get_info_one('5cd2d516db468ac6fbde8c6e', '5cd2a251f9c23996741bdb12'))
    # temp.get_info_like('5cd3bd685d9b1cfdd763ea63')
    # temp.get_info_all()
    # print(temp.get_info_type('food'))
    print(temp.search_by_title('菜'))
