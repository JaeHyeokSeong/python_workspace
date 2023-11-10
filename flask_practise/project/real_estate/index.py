from flask import Blueprint, render_template, session

blue_index = Blueprint('index', __name__)


@blue_index.route('/')
def index():
    return render_template('index.html', session=session)
