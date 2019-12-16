from DBHelper import DBHelper
import re

class Util:
    def __init__(self, img_path, title_prefix):
        self.img_path = img_path
        self.title_prefix = title_prefix

    # poet_poem_list
    def get_parameters_for_topic_from_db(self, category):
        db = DBHelper()
        para_dict = {}

        logo_path = db.get_logo_for_category(category)
        para_dict['logo_path'] = self.img_path + logo_path

        chn_category = db.get_chn_name_for_category(category)
        title = self.title_prefix + chn_category
        para_dict['title'] = title

        para_dict['sliders'] = db.get_slider_info_for_category(chn_category) # slider_list

        # update slider path
        for slider_dict in para_dict['sliders']:
            slider_dict['path'] = self.img_path + slider_dict['path']

        poet_poem_dict = {}
        poet_names = db.get_all_poet_names_for_a_category(chn_category)
        for poet_name in poet_names:
            poet_poem_dict[poet_name] = db.get_all_poems_by_poet_in_category(poet_name, chn_category)

        para_dict['main_content'] = poet_poem_dict
        return para_dict

        # poet_poem_list

    def get_parameters_for_shishe_from_db(self, category):
        db = DBHelper()
        para_dict = {}
        logo_path = db.get_logo_for_category(category)

        para_dict['logo_path'] = self.img_path + logo_path

        chn_category = db.get_chn_name_for_category(category)
        title = self.title_prefix + chn_category
        para_dict['title'] = title

        blog_dict = db.get_blog_dict_of_shishe(category)
        blog_dict['blog_img'] = self.img_path + blog_dict['blog_img']

        para_dict['blog_dict'] = blog_dict
        return para_dict

    # poem_content_page
    def get_parameters_for_poem_content_page(self, category, poem_name):
        db = DBHelper()
        para_dict = {}

        logo_path = db.get_logo_for_category(category)
        para_dict['logo_path'] = self.img_path + logo_path

        title = self.title_prefix + poem_name
        para_dict['title'] = title

        para_dict['main_content'] = db.get_poem_content(poem_name)
        return para_dict

    # Processes text
    def process_text(self, raw_text):
        if not raw_text:
            return ""
        whitespace_removed_text = raw_text.replace(" ", "")
        return whitespace_removed_text

    # Encountered punctuation create a new line
    # Returns a list of poem sentences with punctuation.
    def format_poem_content(self, full_poem):
        full_poem = self.process_text(full_poem)
        processed_list = re.split('(。|？|，|, |\?|!|！|\n|;|；)', full_poem)
        poem_content_list = []
        punctuation_list = ['，', '。', '！','？',',','!','?','；',';']

        for i in range(int(len(processed_list) / 2)):
            punctuation_field = processed_list[2 * i + 1]
            if not punctuation_field:
                poem_content_list.append(processed_list[2 * i])
                break

            if punctuation_field == '\n':
                poem_content_list.append(processed_list[2 * i])
                poem_content_list.append(processed_list[2 * i + 1])
                continue

            if punctuation_field in punctuation_list:
                this_str = processed_list[2 * i] + processed_list[2 * i + 1]
                poem_content_list.append(this_str)
            else:
                print("error: wrong format!")

        return poem_content_list
