from DBHelper import DBHelper

db = DBHelper()
# sql_query = "show tables"
# [{'Tables_in_poemDB': 'Poem'}, {'Tables_in_poemDB': 'Poet'}, {'Tables_in_poemDB': 'Topic'}]
sql_query = "describe Poem"
#
print(db.fetch(sql_query))

# category = "名勝古跡"
# poet_name = "黃火若"
# print(db.get_all_poems_by_poet_in_category(poet_name, category))

# poem_name = "大世界紀遊"
# print(db.get_poem_content(poem_name))

