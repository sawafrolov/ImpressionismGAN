from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object("config")
bootstrap = Bootstrap()
bootstrap.init_app(app)

from app import routes