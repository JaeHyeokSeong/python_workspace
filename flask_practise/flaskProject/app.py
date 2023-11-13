from flask import Flask
from flask import render_template
from course_evaluation import ce

app = Flask(__name__)
app.register_blueprint(ce)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
