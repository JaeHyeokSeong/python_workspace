from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sign-in/', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('sign-in.html')
    else:
        username = request.form['username']
        password = request.form['password']
        print(f'username: {username}, password: {password}')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=8000)
