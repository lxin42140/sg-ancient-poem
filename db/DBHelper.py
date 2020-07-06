import json
import re

import pandas as pd
import pymysql


class DBHelper:

    def __init__(self):
        self.host = "sg-jiutishi-db.ciuqsne5nixf.ap-southeast-1.rds.amazonaws.com"
        self.user = "admin"
        self.password = "?Jiutishi.2019"
        self.port = 3306
        self.charSet = "utf8"
        self.db = "poemDB"
        self.img_path = "/static/images/"
    def __connect__(self):
        try:
            self.con = pymysql.connect(host=self.host, user=self.user, port=self.port, charset=self.charSet,
                                       password=self.password, db=self.db, cursorclass=pymysql.cursors.
                                       DictCursor, autocommit=True)
            self.cur = self.con.cursor()
        except Exception as e:
            print("Exception occurred:{}".format(e))

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

    # encoding json
    def get_db_prep_value(self, value):
        try:
            string = json.dumps(value)
            return re.escape(string)
        except TypeError:
            BAD_DATA.error(
                "cannot serialize %s to store in a JsonField", str(value)
            )
            return ""

    # decoding json
    def get_data_from_db_json_value(self, value):
        if value == "":
            return None
        try:
            return json.loads(value)
        except TypeError:
            BAD_DATA.error("cannot load dictionary field -- type error")
            return None

    def get_author_info_dict_from_db(self, author_name):
        # add poet info
        sql_query = "SELECT yearOfBirth, yearOfDeath, description, source, link, photo_link, photo_desc" \
                    " FROM Poet WHERE fullName = '" + author_name + "'"
        answer_list = self.fetch(sql_query)
        if len(answer_list) > 0:
            answer_dict = answer_list[0]
            if answer_dict["photo_link"]:
                answer_dict["photo_link"] = self.img_path + answer_dict["photo_link"]
            return answer_dict
        else:
            return {}

    # category in chinese
    # ans_dict: key - author_name; value - a dict of poet contains yearOfBirth, yearOfDeath,
    # description, link, photo_link, photo_desc and titles
    def get_poet_info_list_for_a_category(self, category):

        sql_query = "SELECT title, author_name FROM Poem WHERE category = '" + category + "'"
        answer_list = self.fetch(sql_query)
        ans_dict = {}

        for answer in answer_list:
            title = answer['title']
            author_name = answer['author_name']
            if author_name in ans_dict:
                ans_dict[author_name].append(title)
            else:
                ans_dict[author_name] = [title]

        for author_name, titles in ans_dict.items():
            # retrieve poet info from poet db
            new_author_dict = self.get_author_info_dict_from_db(author_name)
            new_author_dict["titles"] = titles
            ans_dict[author_name] = new_author_dict

        return ans_dict

    # category in chinese
    # ans_dict: key - author_name; value - a dict of poet contains yearOfBirth, yearOfDeath,
    # description, link, photo_link, photo_desc, titles
    def get_author_info_list_for_paper(self):
        sql_query = "SELECT title, author FROM Paper"
        answer_list = self.fetch(sql_query)
        ans_dict = {}

        for answer in answer_list:
            title = answer['title']
            author_name = answer['author']
            if author_name in ans_dict:
                ans_dict[author_name].append(title)
            else:
                ans_dict[author_name] = [title]

        for author_name, titles in ans_dict.items():
            # retrieve poet info from poet db
            new_author_dict = self.get_author_info_dict_from_db(author_name)
            new_author_dict["titles"] = titles
            ans_dict[author_name] = new_author_dict

        return ans_dict

    # category in chinese
    # ans_dict: key - author_name; value - a dict of poet contains yearOfBirth, yearOfDeath,
    # description, link, photo_link, photo_desc, titles (list of tuples in the format: (video_name, video_link) ) for embed
    def get_author_info_list_for_video(self):
        sql_query = "SELECT title, author, link FROM Video"
        answer_list = self.fetch(sql_query)
        ans_dict = {}
        
        for answer in answer_list:
            title = (
                answer['title'], answer['link']
            )
            author_name = answer['author']
            if author_name in ans_dict:
                ans_dict[author_name].append(title)
            else:
                ans_dict[author_name] = [title]
                
        for author_name, titles in ans_dict.items():
            # retrieve poet info from poet db
            new_author_dict = self.get_author_info_dict_from_db(author_name)
            new_author_dict["titles"] = titles
            ans_dict[author_name] = new_author_dict

        return ans_dict

    # not using
    def get_all_poet_names_for_a_category(self, category):
        sql_query = "SELECT DISTINCT author_name FROM Poem WHERE category = '" + category + "'"
        answer_list = self.fetch(sql_query)
        ans_list = []
        for answer in answer_list:
            ans_list.append(answer['author_name'])
        return ans_list

    # not using
    # category in chinese
    def get_all_poems_by_poet_in_category(self, poet_name, category):
        sql_query = "SELECT DISTINCT title FROM Poem WHERE category = '" + category + "' AND author_name = '" + poet_name + "'"
        answer_list = self.fetch(sql_query)
        ans_list = []
        for answer in answer_list:
            ans_list.append(answer['title'])
        return ans_list

    def get_poem_content(self, poem_name, author_name):
        sql_query = "SELECT title, year, author_name, introduction, content, published_info, comments FROM " \
                    "Poem WHERE title = '" + poem_name + "' AND author_name = '" + author_name + "'"
        content_dict = self.fetch(sql_query)[0]
        return content_dict

    def get_paper_content(self, paper_title, author_name):
        sql_query = "SELECT title, author, link FROM Paper WHERE title = '" + paper_title + "' AND author = '" + author_name + "'"
        content_dict = self.fetch(sql_query)[0]
        return content_dict

    def get_logo_for_category(self, category):
        sql_query = "SELECT logo_url FROM Topic WHERE name = '" + category + "'"
        try:
            fetch_result = self.fetch(sql_query)
            logo_url = fetch_result[0]['logo_url']
            return logo_url
        except Exception as e:
            print("Getting logo for category....")
            print("Exception occurred:{}".format(e))
            print("Category name:{}".format(category))


    def get_chn_name_for_category(self, category):
        sql_query = "SELECT chn_name FROM Topic WHERE name = '" + category + "'"
        chn_name = self.fetch(sql_query)[0]['chn_name']
        return chn_name

    # Return format:
    # sliders = [
    #     {
    #         'path': IMG_PATH + 'slider-1.jpg',
    #         'comments': ['星洲四大才子', '葉季允, 釋瑞于, 邱菽園, 李俊承', '1859 - 1966']
    #     },
    #     {
    #         'path': IMG_PATH + 'slider-2.jpg',
    #         'comments': ['烏敏島油畫', '何自力  作', '新加坡國立大學中文系講師']
    #     }
    # ]
    def get_slider_info_for_category(self, category):
        sql_query = "SELECT slider FROM Topic WHERE chn_name = '" + category + "'"
        db_json = self.fetch(sql_query)[0]['slider']
        if not db_json:
            return ""

        raw_data = self.get_data_from_db_json_value(db_json)
        type = raw_data['slider_type']

        slider_list = []
        if type == 1:
            slider_dict = raw_data['urls_dict']

            for key, value in slider_dict.items():
                ans_dict = {}
                ans_dict['path'] = key
                ans_dict['comments'] = value
                slider_list.append(ans_dict)

        # wip: need to modify the structure in the db
        elif type == 0:
            # zhuanti
            ans_dict = {}
            ans_dict['path'] = raw_data['urls'][0]
            ans_dict['comments'] = ''
            slider_list.append(ans_dict)
        return slider_list

    # return a blog dictionary
    def get_blog_dict_of_shishe(self, shishe_name):
        sql_query = "SELECT blog_title, blog_content, blog_img, blog_link FROM Topic WHERE name = '" + shishe_name + "'"
        blog_dict = self.fetch(sql_query)[0]
        return blog_dict


        return blog_dict

    # update slider column in topic db
    def save_slider_to_db(self, slider_string, topic_id):
        try:
            this_item = self.get_db_prep_value(slider_string)
            sqlQuery = "UPDATE Topic SET slider = '{}' WHERE id = {}".format(this_item, topic_id)
            self.execute(sqlQuery)
            return True
        except Exception as e:
            print("Exeception occured:{}".format(e))
            return False
