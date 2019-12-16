from flask import Flask, render_template
from DBHelper import DBHelper
import re

app = Flask(__name__)

IMG_PATH = '../static/images/'
title_prefix = '新加坡舊體詩庫-'

@app.route('/')
@app.route('/home')
def home():
    logo_path = IMG_PATH + 'logo.png'
    title = '新加坡舊體詩庫'
    sliders = [  # fake array of posts
        {
            'path': IMG_PATH + 'slider-1.jpg',
            'comments': ['星洲四大才子', '葉季允, 釋瑞于, 邱菽園, 李俊承', '1859 - 1966']
        },
        {
            'path': IMG_PATH + 'slider-2.jpg',
            'comments': ['烏敏島油畫', '何自力  作', '新加坡國立大學中文系講師']
        }
    ]
    return render_template('homepage.html',
       title = title,
       logo_path = logo_path,
       sliders = sliders)

# poet_poem_list
def get_parameters_for_main_category(category):
    db = DBHelper()
    para_dict = {}

    logo_path = db.get_logo_for_category(category)
    para_dict['logo_path'] = IMG_PATH + logo_path

    chn_category = db.get_chn_name_for_category(category)
    title = title_prefix + chn_category
    para_dict['title'] = title

    para_dict['sliders'] = db.get_slider_info_for_category(chn_category) # slider_list

    # update slider path
    for slider_dict in para_dict['sliders']:
        slider_dict['path'] = IMG_PATH + slider_dict['path']

    poet_poem_dict = {}
    poet_names = db.get_all_poet_names_for_a_category(chn_category)
    for poet_name in poet_names:
        poet_poem_dict[poet_name] = db.get_all_poems_by_poet_in_category(poet_name, chn_category)

    para_dict['main_content'] = poet_poem_dict
    return para_dict

# poem_content_page
def get_parameters_for_poem_content_page(category, poem_name):
    db = DBHelper()
    para_dict = {}

    logo_path = db.get_logo_for_category(category)
    para_dict['logo_path'] = IMG_PATH + logo_path

    title = title_prefix + poem_name
    para_dict['title'] = title

    para_dict['main_content'] = db.get_poem_content(poem_name)
    return para_dict


# Encountered punctuation create a new line
# Returns a list of poem sentences with punctuation.
def format_poem_content(full_poem):
    processed_list = re.split('(。|？|，|, |\?)', full_poem)
    poem_content_list = []

    for i in range(int(len(processed_list) / 2)):
        if processed_list[2 * i + 1]:
            this_str = processed_list[2 * i] + processed_list[2 * i + 1]
            poem_content_list.append(this_str)
    return poem_content_list

# Processes text
def process_text(raw_text):
    if not raw_text:
        return ""
    whitespace_removed_text = raw_text.replace(" ", "")
    line_breaker_removed_text = whitespace_removed_text.replace("\n", "")
    return line_breaker_removed_text


@app.route('/category/<category>', methods=['GET'])
def topic(category):
    para_dict = get_parameters_for_main_category(category)

    return render_template('slider-poem-list.html',
       category = category,
       title = para_dict['title'],
       logo_path = para_dict['logo_path'],
       sliders = para_dict['sliders'],
       main_content = para_dict['main_content'],
    )

@app.route('/<category>/<poem_name>', methods=['GET'])
def poem_content_page(category, poem_name):
    para_dict = get_parameters_for_poem_content_page(category, poem_name)
    full_poem = para_dict['main_content']['content']
    introduction = process_text(para_dict['main_content']['introduction'])
    poem_content_list = format_poem_content(full_poem)

    return render_template('poem-content.html',
       title = para_dict['title'],
       logo_path = para_dict['logo_path'],
       main_content = para_dict['main_content'],
       introduction = introduction,
       poem_content_list = poem_content_list,
    )

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return ""

@app.route("/<any>", methods=['GET', 'POST'])
def any_to_404(any):
    return render_template('base.html'), 404

# @app.errorhandler(404)
# def notfound():
#     """Serve 404 template."""
#     return make_response(render_template("404.html"), 404)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)