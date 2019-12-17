from DBHelper import DBHelper

db = DBHelper()

# sql_query = "INSERT INTO Topic (id, name, chn_name, logo_url) VALUES (9, 'zhuanti-nanyangdaxue', '南洋大學師生作品', 'logo-nanyangdaxue.png');"
# # sql_query = "UPDATE `Topic` SET `blog_title` = '新嘉坡風土記(1936)' WHERE `id` = 11;"
# db.execute(sql_query)

# sql_query = "ALTER TABLE Topic ADD blog_content TEXT"
# db.execute(sql_query)

# sql_query = "show tables"
# [{'Tables_in_poemDB': 'Poem'}, {'Tables_in_poemDB': 'Poet'}, {'Tables_in_poemDB': 'Topic'}]
# sql_query = "describe Topic"
# sql_query = "SELECT id, name, chn_name, logo_url, slider from Topic WHERE id = 8;"
# sql_query = "SELECT * FROM Topic;"
# sql_query = "INSERT INTO Topic (id, name, chn_name, logo_url) VALUES (24, 'wenyihuodong', '文藝活動', 'logo-wenyihuodong.png');"
# sql_query = "UPDATE Poem SET category = replace(category, '文化藝術活動', '文藝活動')"
# db.execute(sql_query)
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

# sql_query = "UPDATE Poem SET category = replace(category, '南洋物產', '南洋風土')"
# db.execute(sql_query)
# sql_query = "SELECT * FROM Poem WHERE category = '南洋風土'"
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


# category = "大專文學獎漢詩組"
# print(db.get_slider_info_for_category(category))


# category "名勝古跡"
# [{'path': 'slider-mingshengguji-1.jpg',
#   'comments': ['濱海灣', '魚尾獅', '1965-2019']},
#  {'path': 'slider-shuanglin.jpg',
#   'comments': ['184 Jalan Toa Payoh, Singapore 319944', '雙林寺']
# }]

# {'slider_type': 0, 'urls': ['slider-dazhuan.png']}