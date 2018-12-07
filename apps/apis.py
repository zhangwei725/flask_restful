from flask_restful import Api

from apps.main.api import IndexResource

api = Api(prefix='/api/v2')


def init_api(app):
    api.init_app(app=app)


"""
参数一  在api中写的resource对象
参数二  *urls

 **kwargs
"""

api.add_resource(IndexResource,
                 '/',
                 '/index/')
