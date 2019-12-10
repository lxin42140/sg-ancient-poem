from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    logo_path = "../static/images/logo.png"
    title = '新加坡舊體詩庫'
    return render_template('01-homepage.html',
                           title = title,
                           logo_path = logo_path)

@app.route('/zhuanti')
def topic():
    logo_path = "../static/images/logo-chunlian.png"
    title = '新加坡舊體詩庫-大專文學獎漢詩組'
    return render_template('02-zhuanti.html',
                           title = title,
                           logo_path = logo_path)

@app.route('/mingshengguji')
def mingsheng():
    logo_path = "xx"
    title = 'xx'
    return render_template('03-mingshengguji.html',
                           title = title,
                           logo_path = logo_path)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)