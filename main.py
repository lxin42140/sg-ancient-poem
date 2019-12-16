from flask import Flask, render_template
from Util import Util

app = Flask(__name__)
IMG_PATH = '../static/images/'
title_prefix = '新加坡舊體詩庫-'
util = Util(IMG_PATH, title_prefix)


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


@app.route('/category/<category>', methods=['GET'])
def topic(category):
    para_dict = util.get_parameters_for_topic_from_db(category)

    return render_template('slider-poem-list.html',
       category = category,
       title = para_dict['title'],
       logo_path = para_dict['logo_path'],
       sliders = para_dict['sliders'],
       main_content = para_dict['main_content'],
    )

@app.route('/shishe/<name>', methods=['GET'])
def shishe(name):
    para_dict = util.get_parameters_for_shishe_from_db(name)
    # if not para_dict:
    #     return "{} gots nothing".format(name)
    blog_dict = para_dict['blog_dict']
    return render_template('blog.html',
       logo_path=para_dict['logo_path'],
       title=para_dict['title'],
       blog_title = blog_dict['blog_title'],
       blog_content = blog_dict['blog_content'],
       blog_img = blog_dict['blog_img'],
       blog_link = blog_dict['blog_link'],
    )

@app.route('/<category>/<poem_name>', methods=['GET'])
def poem_content_page(category, poem_name):
    para_dict = util.get_parameters_for_poem_content_page(category, poem_name)
    full_poem = para_dict['main_content']['content']
    introduction = util.process_text(para_dict['main_content']['introduction'])
    poem_content_list = util.format_poem_content(full_poem)

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