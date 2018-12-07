from flask import Flask

# 程序的入口
from apps.apis import init_api
from apps.ext import init_ext
from apps.hello.views import hello


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456789'
    app.debug = True
    init_api(app)
    init_ext(app)
    return app


def register(app: Flask):
    app.register_blueprint(hello)
