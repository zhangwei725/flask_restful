from flask import request
from flask_restful import Resource, reqparse

from apps.main.models import User


class CateResource(Resource):
    def __init__(self):
        # 添加参数
        # 解析参数
        self.parser = reqparse.RequestParser()
        """
        :argument  参数的key
        :type  参数的类型
        :default 默认值
        """
        # page
        # size
        self.parser.add_argument('page', type=int, default=1)
        self.parser.add_argument('size', type=int, default=10)

    def get(self):
        """
        key,
        default=None,
        type=None  数据类型
        :return:
        """
        # 字典类型
        # /?page=1&size=20
        # {
        #     'page':1,
        #     'size':20
        # }
        args = self.parser.parse_args()
        page = args.get('page')
        size = args.get('size')
        return '基本参数'


"""
必要参数

"""


class RequiredResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('uid', type=int, required=True, help='uid参数必传')
        self.parser.add_argument('path', type=str, required=True, help='路径不能为空')
        self.parser.add_argument('status', type=int)
        # 一键多值
        self.parser.add_argument('name', type=str, action='append')
        #     位置参数
        self.parser.add_argument('token', type=str, location='headers')

    def put(self):
        # request.args
        # request.form  put  post
        token = request.headers.get('token')
        c = request.headers.get('Cache-Control')
        args = self.parser.parse_args()
        uid = args.get('uid')
        path = args.get('path')
        status = args.get('status')
        names = args.get('name')
        user = User.query.get(uid)
        user.image = path
        user.status = status

        return {'hello': 'world'}

# 多值操作   一键多值
# name='xiaoming'&name='xiaohua'& name='娇娇'
