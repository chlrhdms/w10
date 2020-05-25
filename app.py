from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return '메인페이지'

@app.route('/move/<name>')
def input_name(name):
    if name == 'naver':
        return redirect(url_for('naver'))
    elif name == 'daum':
        return redirect(url_for('daum'))
    else:
        return "없는 사이트"

@app.route('/naver')
def naver():
    return render_template("naver.html")

@app.route('/daum')
def daum():
    return redirect("https://www.daum.net/")

if __name__ == '__main__':
    app.run(debug=True)