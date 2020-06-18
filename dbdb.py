import sqlite3

def dbcon():
    return sqlite3.connect('mydb.db')

# users 테이블 생성 함수
def create_table():
    try:
        qiery = '''
            CREATE TABLE "users" (
            	"id"	varchar(50),
            	"pw"	varchar(50),
            	"name"	varchar(50),
            	PRIMARY KEY("id")
        );
        '''
        db = dbcon()
        c = db.cursor()
        c.execute(qiery)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def insert_user(id, pw):
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id, pw)
        c.execute("INSERT INTO users VALUES (?, ?)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def select_user(id, pw):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id, pw)
        c.execute('SELECT * FROM users WHERE id = ? AND pw = ?', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret

# create_table()
# insert_user('abc', '1234', '에비시')
# insert_data('20201236', '디비')
# ret = select_all()
# ret = select_num('20201236')
# ret = select_user('abc', '1234')
# print(ret)
