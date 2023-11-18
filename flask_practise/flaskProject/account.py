from flask import Blueprint, request, render_template, redirect, url_for

ac = Blueprint('ac', __name__, url_prefix='/account')


# sign in 구현하기
@ac.route('/signIn/', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('signIn.html')
    else:
        user_email = request.form['user_email']
        user_password = request.form['user_password']
        print(f'TEST: {user_email}, {user_password}')
        return redirect(url_for('index'))


# create account 구현하기
@ac.route('/create_account/', methods=['GET', 'POST'])
def create_account():
    if request.method == 'GET':
        return render_template('create_account.html')
    else:
        user_email = request.form['user_email']
        user_password = request.form['user_password']
        university = request.form['university']
        major = request.form['major']

        # db 에 입력되어진 사용자 정보 저장하기

        return redirect(url_for('index'))
