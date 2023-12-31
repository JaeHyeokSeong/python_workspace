from flask import Flask
from flask import render_template
from course_evaluation import ce
from account import ac

app = Flask(__name__)
app.register_blueprint(ce)
app.register_blueprint(ac)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
