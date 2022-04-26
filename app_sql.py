from flask import Flask, render_template, jsonify, request, session
from flask import current_app
from oauth2client.contrib.flask_util import UserOAuth2
from dao import Database2
import hashlib


app = Flask(__name__)
app.secret_key = 'aaa!111/'

app.config['SECRET_KEY'] = 'aaa!111/'

# API 사용을 위해서 아래와 같이 관련 정보를 담은 json 파일(개발자 페이지에서 받을 수 있다)을 사용할 수 있고,
# app.config['GOOGLE_OAUTH2_CLIENT_SECRETS_FILE'] = 'client_secret_880960686462-ng2l9g8jcv8ahhpr9iftrb1neecihe5b.apps.googleusercontent.com.json'

# 이렇게 코드에 직접 넣을 수도 있다.
app.config['GOOGLE_OAUTH2_CLIENT_ID'] = '880960686462-ng2l9g8jcv8ahhpr9iftrb1neecihe5b.apps.googleusercontent.com'
app.config['GOOGLE_OAUTH2_CLIENT_SECRET'] = 'jKbsqwUxXCve1si9ypy4gQbe'

oauth2 = UserOAuth2(app)


# 통계 화면으로 이동
@app.route('/', methods=['get'])
def getblank1():
    return render_template('home.html') 

@app.route('/mypage', methods=['get'])
def getmypage():
    return render_template('mypage.html')  

@app.route('/quit', methods=['get'])
def getquit():
    return render_template('quit.html')  

@app.route('/next', methods=['get'])
def getnext():
    return render_template('next.html')  
    
# 그루스크롤 화면으로 이동
@app.route('/blank1', methods=['get'])
def gethome():
    return render_template('blank1.html')  

# 팀원소개 화면으로 이동
@app.route('/introduce', methods=['get'])
def getintroduce():
    return render_template('introduce.html')  

# 팀원소개 화면으로 이동
@app.route('/start', methods=['get'])
def getstart():
    return render_template('start.html')  

# mbti 화면으로 이동
@app.route('/mbti', methods=['get'])
def getmbti():
    return render_template('mbti.html')  

# 소개(시바견그림) 화면으로 이동
# @app.route('/', methods=['get'])
# def getindex():
#     return render_template('index.html')  

# 쇼핑몰로 이동
@app.route('/shop', methods=['get'])
def getshop():
    return render_template('shop.html')  

# 회원가입 화면으로 이동
@app.route('/sign', methods=['get'])
def getjoin():
    return render_template('join.html')  

# 로그인 화면으로 이동
@app.route('/login', methods=['get'])
def getlogin():
    return render_template('login.html')  

# 회원가입 기능
@app.route('/sign_in', methods=['POST'])
def sign_in():
    # "id=" + id + "&pw=" + pw + "&name=" + name + "&email=" + email
    id = request.form.get('id')
    pw = request.form.get('pw')
    name = request.form.get('name')
    email = request.form.get('email')
    pw = hashlib.sha256(pw.encode())
    pw = pw.hexdigest()
    print(pw)
    data = (id, pw, name, email)
    print(Database2.email_check(email))
    if Database2.email_check(email) != None:
        return '이미 가입된 이메일 입니다.'
    if Database2.id_check(id) != None:
        return '중복된 아이디입니다.'
    else:
        Database2.insertdb(data)
        return  '가입완료!!'

# 회원탈퇴
@app.route('/sign_quit', methods=['POST'])
def withdraw():
    id = request.form.get('id')
    pw = request.form.get('pw')
    idpw = (id, pw)

    if Database2.logindb(idpw) != None:
        Database2.deletedb(id)
        session.clear()
        return "회원탈퇴가 완료되었습니다!"
    else:
        return "아이디나 비밀번호가 일치하지 않습니다"


# 로그인 기능
@app.route('/login_check', methods=['POST'])
def login_check():
    id = request.form.get('id')
    pw = request.form.get('pw')
    pw = hashlib.sha256(pw.encode('utf-8'))
    pw = pw.hexdigest()
    idpw = (id, pw)
    session.clear()

    # id/pw가 테이블에 존재하면 세션만들기
    if Database2.logindb(idpw) != None:
        print(session)
        session.clear()
        session['user'] = id
        print(session)
        return "로그인이 완료되었습니다!"
    else:
        return "아이디나 비밀번호가 일치하지 않습니다"

# 구글 소셜로그인
@app.route('/google', methods=['GET'])
@oauth2.required
def google():
    print("구글로그인=============================")
    request.headers.get('Allow-Control-Allow-Origin: *')
    # response.headers['Authorization'] = 'Allow-Control-Allow-Origin: *'
    return '구글로그인 되나'

# @app.route('/google')
# @oauth2.required
# def info():
#     # return "Hello, {} ({})".format(oauth2.email, oauth2.user_id)
#     return "구글로그인 되나"

# @app.route('/google')
# def google():
#     print(oauth2.authorize_url)
#     return oauth2.authorize_url("/")


# 로그아웃 기능
@app.route('/logout_check', methods=['get'])
def logout():
    session.clear()
    # session.pop("user")
    print("로그아웃")
    return '로그아웃 되었습니다!'


# 세션 아이디를 조회하여 마이 페이지에 정보 출력
@app.route('/usercheck', methods=['POST'])
def usercheck():
    id = request.form.get('id')
    data = (id,)
    print(data)
    return Database2.select(data)

@app.route('/order', methods=['POST'])
def order2():
    p_name = request.form.get('p_name')
    p_price = request.form.get('p_price')
    id = request.form.get('id')
    data = (p_name, p_price, id)
    print(data)
    Database2.insertdb2(data)
    
    return '주문을 완료하였습니다!!'

@app.route('/vieworder', methods=['POST'])
def vieworder():

    id = request.form.get('id')
    data = (id,)
    print(data)
    
    return Database2.view_order(data)



if __name__ == "__main__":
    # app.run(debug=True, host="127.0.0.1", port="5000")
    app.run(debug=True, host="0.0.0.0", port="5000")