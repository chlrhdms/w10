from flask import Flask, request, render_template, redirect, url_for, abort, session

import game
import json
import dbdb
import random

app = Flask(__name__)

app.secret_key = b'aaa!111/'

@app.route('/')
def index():
    return render_template('main.html')

#게임(시작)
@app.route('/gamestart')
def gamestart():
    if 'user' in session:
        with open("static/save.txt", "r", encoding='utf-8') as f:
            date = f.read()
            character = json.loads(date)
        return render_template('gamestart.html', data=character)
    return redirect(url_for('login'))

#게임(진행)
@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        with open("static/save.txt", "r", encoding='utf-8') as f:
            date = f.read()
            character = json.loads(date)
            print(character['items'])
        return "{}님이 {}(으)로 공격했습니다<br><button type='button' class='btn btn-danger'><a class='nav-link' href=/gamestart>다음</a></button>".format(character['name'], random.choice(character["items"]))
    elif num == 2:
        with open("static/save.txt", "r", encoding='utf-8') as f:
            date = f.read()
            character = json.loads(date)
            print(character['skill'])
        return "{}님이 {}(으)로 방어했습니다<br><button type='button' class='btn btn-danger'><a class='nav-link' href=/gamestart>다음</a></button>".format(character['name'], random.choice(character["skill"]))
    elif num == 3:
        with open("static/save.txt", "r", encoding='utf-8') as f:
            date = f.read()
            character = json.loads(date)
            print(character['run'])
        return "{}님이 도망에 {} 했습니다<br><button type='button' class='btn btn-danger'><a class='nav-link' href=/gamestart>다음</a></button>".format(character['name'], random.choice(character["run"]))
    
    # return "hello {}".format(name)

#로그인
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
        print(ret)
        if ret != None:
            session['user'] = id
            game.set_charact(ret[2])
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

#로그아웃
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

#회원가입
@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        name = request.form['name']
        print (id,type(id))
        print (pw,type(pw))
        ret = dbdb.check_id(id)
        if ret != None:
            return '''
                    <script>
                    alert('다른 아이디를 사용하세요');
                    location.href='/join';
                    </script>

                    '''
        # id와 pw가 db 값이랑 비교 해서 맞으면 맞다 틀리면 틀리다
        dbdb.insert_user(id, pw, name)
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)