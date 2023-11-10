from flask import Flask
from .login import blue_login
from .index import blue_index

app = Flask(__name__)
app.register_blueprint(blue_login)
app.register_blueprint(blue_index)
