from DBHelper import DBHelper

db = DBHelper()
# sql_query = "show tables"
# [{'Tables_in_poemDB': 'Poem'}, {'Tables_in_poemDB': 'Poet'}, {'Tables_in_poemDB': 'Topic'}]
# sql_query = "describe Topic"
# [{'Field': 'id', 'Type': 'int(11)', 'Null': 'NO', 'Key': 'PRI', 'Default': None, 'Extra': ''},
#  {'Field': 'name', 'Type': 'varchar(32)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''},
#  {'Field': 'chn_name', 'Type': 'varchar(32)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''},
#  {'Field': 'logo_url', 'Type': 'varchar(256)', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''},
#  {'Field': 'slider', 'Type': 'text', 'Null': 'YES', 'Key': '', 'Default': None, 'Extra': ''}
#  ]

# sql_query = "select name from Topic"
# [{'name': 'zhuanti-chunlian'},
#  {'name': 'zhuanti-dazhuan'},
#  {'name': 'zhuanti-nus'},
#  {'name': 'zhuanti-sgyinglian'},
#  {'name': 'zhuanti-shuanglin'},
#  {'name': 'zhuanti-xinzhouyayuan'},
#  {'name': 'mingshengguji'},
#  {'name': 'nanyangfengsu'},
#  {'name': 'difangyuyan'},
#  {'name': 'nanyangwuchan'},
#  {'name': 'xingzhoufengyue'},
#  {'name': 'foyuchanxin'},
#  {'name': 'lunxianshiqi'},
#  {'name': 'quanqiuhanshizonghui'},
#  {'name': 'shichengyinshe'},
#  {'name': 'tanshe'},
#  {'name': 'xinshengshishe'},
#  {'name': 'shiji'},
#  {'name': 'shirenfangtan'},
#  {'name': 'shirenshengping'},
#  {'name': 'shirenyinchang'},
#  {'name': 'shitanjinkuang'},
#  {'name': 'yanjiulunwen'}]


# print(db.fetch(sql_query))

# category = "名勝古跡"
# poet_name = "黃火若"
# ans = db.get_all_poems_by_poet_in_category(poet_name, category)
# print(ans)
# print(db.get_all_poems_by_poet_in_category(poet_name, category))

# poem_name = "大世界紀遊"
# print(db.get_poem_content(poem_name))

# category = "名勝古跡"
# print(db.get_logo_for_category(category))
#
# category = "zhuanti-dazhuan"
# print(db.get_chn_name_for_category(category))


category = "大專文學獎漢詩組"
print(db.get_slider_info_for_category(category))



# category "名勝古跡"
# [{'path': 'slider-mingshengguji-1.jpg',
#   'comments': ['濱海灣', '魚尾獅', '1965-2019']},
#  {'path': 'slider-shuanglin.jpg',
#   'comments': ['184 Jalan Toa Payoh, Singapore 319944', '雙林寺']
# }]

# {'slider_type': 0, 'urls': ['slider-dazhuan.png']}