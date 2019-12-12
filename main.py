from flask import Flask, render_template
app = Flask(__name__)

IMG_PATH = '../static/images/'

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

@app.route('/zhuanti')
def topic():
    logo_path = IMG_PATH + 'logo-chunlian.png'
    title = '新加坡舊體詩庫-大專文學獎漢詩組'
    poems = []
    return render_template('zhuanti.html',
                           title = title,
                           logo_path = logo_path,
                           poems = poems)

@app.route('/mingshengguji')
def mingsheng():
    logo_path = "xx"
    title = '新加坡舊體詩庫-名勝古跡'
    sliders = [  # fake array of posts
        {
            'path': IMG_PATH + 'slider-mingshengguji-1.jpg',
            'comments': ['濱海灣', '魚尾獅', '1965-2019']
        },
        {
            'path': IMG_PATH + 'slider-shuanglin.jpg',
            'comments': ['184 Jalan Toa Payoh', '雙林寺', 'Singapore 319944']
        }
    ]
    return render_template('slider-poem-list.html',
                           title = title,
                           logo_path = logo_path,
                           sliders = sliders)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)