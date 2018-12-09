from flask_restful import Resource, fields, marshal_with

from apps.home.models import Banner

"""
接口文档


"""

"""
定义Resource
定义数据格式
请求接口关联数据模板  @marshal_with()
填充数据返回 自动转化json数据



{
"status':200
'msg':'success'
data:[
]
{
"status':200
'msg':'success'
data:{
    com:'a',
    'obj':{
    
    },
    users:[
        {},
        {},
    ]
}
}


"""
# {
# "status':200
# 'msg':'success'
# data:[
# {},
# {}
# ]
# }
# 嵌套类型  Nested

banner_fields = {
    'bid': fields.Integer(default=1),
    'path': fields.String
}

result = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(banner_fields))
}


class BannerResource(Resource):
    @marshal_with(fields=result)
    def get(self):
        banners = Banner.query.all()
        result = {
            'status': 200,
            'msg': 'success',
            'data': banners
        }
        return result

    def post(self):
        pass

    def put(self):
        pass


# https://api.apiopen.top/musicBroadcastingDetails?channelname=public_tuijian_spring
# https://api.apiopen.top/videoCategory
cate_fields = {
    'cate_id': fields.Integer,
    'name': fields.String,
}

data_fields = {
    'obj': fields.Nested(),
    'banners': fields.List(fields.Nested()),
    'cates': fields.List(fields.Nested(cate_fields)),
    'hots': fields.List(fields.Nested()),
}


# result = {
#     'status': 200,
#     'msg': 'success',
#     'data': {
#             'obj':{}
#         'banners': [],
#         'cates': []
#          'navis':[]
#          'hots':[]
#
#     }
#
# }
# request
# from  args   headers  cookies  files


class HeadResource(Resource):
    def get(self):
        pass
