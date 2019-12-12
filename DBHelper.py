import pymysql
import pandas as pd
import json

class DBHelper:

    def __init__(self):
        self.host = "sg-jiutishi-db.ciuqsne5nixf.ap-southeast-1.rds.amazonaws.com"
        self.user = "admin"
        self.password = "?Jiutishi.2019"
        self.port = 3306
        self.charSet = "utf8"
        self.db = "poemDB"

    def __connect__(self):
        try:
            self.con = pymysql.connect(host=self.host, user=self.user, port=self.port, charset=self.charSet,
                                       password=self.password, db=self.db, cursorclass=pymysql.cursors.
                                       DictCursor, autocommit=True)
            self.cur = self.con.cursor()
        except Exception as e:
            print("Exeception occured:{}".format(e))

    def __disconnect__(self):
        self.con.close()

    def fetch(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.__disconnect__()
        return result

    def execute(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        self.__disconnect__()

    def get_db_prep_value(value):
        try:
            return json.dumps(value)
        except TypeError:
            BAD_DATA.error(
                "cannot serialize %s to store in a JsonField", str(value)
            )
            return ""

    def get_data_from_db_json_value(value):
        if value == "":
            return None
        try:
            return json.loads(value)
        except TypeError:
            BAD_DATA.error("cannot load dictionary field -- type error")
            return None

    def get_all_poet_names_for_a_category(self, category):
        sql_query = "SELECT DISTINCT author_name FROM Poem WHERE category = '" + category + "'"
        print(sql_query)
        answer_list = self.fetch(sql_query)
        ans_list = []
        for answer in answer_list:
            ans_list.append(answer['author_name'])
        return ans_list

    def get_all_poems_by_poet_in_category(self, poet_name, category):
        sql_query = "SELECT DISTINCT title FROM Poem WHERE category = '" + category + "' AND author_name = '" + poet_name + "'"
        print(sql_query)
        answer_list = self.fetch(sql_query)
        ans_list = []
        for answer in answer_list:
            ans_list.append(answer['title'])
        return ans_list

    def get_poem_content(self, poem_name):
        content_dict = {}
        sql_query = "SELECT DISTINCT content FROM Poem WHERE title = '" + poem_name + "'"
        print(sql_query)
        answer_list = self.fetch(sql_query)
        ans_list = []
        for answer in answer_list:
            ans_list.append(answer['content'])
        return ans_list