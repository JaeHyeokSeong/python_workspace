from flask import Blueprint, request, \
    render_template, redirect, url_for, session
from .models.users import User
blue_login = Blueprint('login', __name__, url_prefix='/')

# memory database
users_db = []

@blue_login.route('sign-in/', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('sign-in.html')
    else:
        username = request.form['username']
        password = request.form['password']
        print(f'username: {username}, password: {password}')

        # user_db 에서 존재하는 username 그리고 password 인지 확인하기
        for user in users_db:
            # user_db 에서 username 그리고 password 가 발견됨
            if user.find_user(username, password):
                session['username'] = username
                return redirect(url_for('index.index'))

        # user_db 에서 username 그리고 password 가 발견안됨
        return render_template('sign-in.html', sign_in_fail='True')

@blue_login.route('sign-out/', methods=['POST'])
def sign_out():
    # remove the username from the session
    session.pop('username', None)
    return redirect(url_for('index.index'))


@blue_login.route('join/', methods=['GET', 'POST'])
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else:
        username = request.form['username']
        password = request.form['password']
        print(f'TEST: joined - username: {username}, password: {password}')

        # username 이 이미 사용중인지 확인하기
        for user in users_db:
            # 이미 사용되어지고 있는 username 그리고 password
            if user.find_username(username):
                return render_template('join.html', duplicate_join='True')

        # 사용가능한 username 그리고 password
        users_db.append(User(username, password))
        return redirect(url_for('index.index'))
