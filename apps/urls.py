from flask_restful import Api

from apps.main.api import IndexResource
from apps.news.api import CateResource, RequiredResource

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
# api.add_resource(BannerResource, '/banners/')
api.add_resource(CateResource, '/cates/')
api.add_resource(RequiredResource, '/required/')
