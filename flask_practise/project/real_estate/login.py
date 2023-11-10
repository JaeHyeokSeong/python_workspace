from flask import Blueprint, request, render_template, redirect, url_for

blue_login = Blueprint('login', __name__, url_prefix='/')


@blue_login.route('sign-in/', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('sign-in.html')
    else:
        username = request.form['username']
        password = request.form['password']
        print(f'username: {username}, password: {password}')
        return redirect(url_for('index.index'))
