from flask import Flask, request, render_template, redirect, url_for, abort, session

import game
import json
import dbdb

app = Flask(__name__)

app.secret_key = b'aaa!111/'

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/hello/')
def hello():
    return ('Hello, World')

@app.route('/hello/<name>')
def hellovar(name):
    character = game.set_charact(name)
    return render_template('gamestart.html', data=character)

@app.route('/gamestart')
def gamestart():
    with open("static/save.txt", "r", encoding='utf-8') as f:
        date = f.read()
        character = json.loads(date)
        print(character['items'])
    return "{}이 {} 아이템을 사용해서 이겼습니다".format(character['name'], character["items"][0])

@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        with open("static/save.txt", "r", encoding='utf-8') as f:
            date = f.read()
            character = json.loads(date)
            print(character['items'])
        return "{}이 {} 아이템을 사용했습니다".format(character['name'], character["items"][0])
    elif num == 2:
        return '도망갔다'
    elif num == 3:
        return '퉁퉁이'
    else: 
        return "없어요"
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
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

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

@app.route('/form')
def form():
    return render_template('test.html')

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET 으로 전송이다.'
    else:
        num = request.form['num']
        name = request.form['name']
        print(num, name)
        dbdb.insert_data(num, name)
        return 'POST 이다. 학번: {} 이름:{}'.format(num,name)

@app.route('/getinfo') 
def getinfo():
    if 'user' in session:
        ret = dbdb.select_all()
        print(ret[3])
        return render_template('getinfo.html', data=ret)

    return redirect(url_for('login'))


if __name__ == '__main__':
    # with app.test_request_context():
    #       print(url_for('daum'))
    app.run(debug=True)
