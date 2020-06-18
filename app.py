from flask import Flask, request, render_template

import game
import json
import dbdb

app = Flask(__name__)

@app.route('/')
def indaex():
    return '메인페이지'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        print (id,type(id))
        print (pw,type(pw))
        # id와 pw가 db 값이랑 비교 해서 맞으면 맞다 틀리면 틀리다
        ret = dbdb.select_user(id, pw)
        if ret != None:
            return "안녕하세요~ {} 님" .format(id)
        else:
            return "아이디 또는 패스워드를 확인 하세요."


if __name__ == '__main__':
    app.run(debug=True)