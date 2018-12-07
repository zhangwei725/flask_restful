from flask_restful import Resource, fields, marshal_with

from apps.ext import db
from apps.main.models import User

"""
第一步定义返回数据的模板
{
'status':200,
'msg':'sucess',
'data':{
    user_id:1
    username:'test'
    price:1.00
}
}
"""

user_fields = {
    'user_id': fields.Integer,
    'username': fields.String,
    'price': fields.Float,
}

result = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(user_fields))
}


class IndexResource(Resource):
    @marshal_with(fields=result)
    def get(self):
        user = User.query.all()
        return {'status': 200, 'msg': 'success', 'data': user}

    def post(self):
        db.session.add_all(
            [User(username=f'test{i}') for i in range(1, 10)]
        )
        db.session.commit()
        return {'hello': 'post'}

    def put(self):
        return {'hello': 'put'}

    def delete(self):
        return {'hello': 'delete'}
