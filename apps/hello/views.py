from flask import Blueprint, jsonify

hello = Blueprint('hello', __name__)
"""
                  json
基本类型           
字典------        对象
列表------>       数组
bool------->>     true  false
None               null

# 对象不能转化成json对象
"""


# restful

@hello.route('/index.html')
def index():
    result = jsonify({'status': 200, 'msg': 'success', 'date': [1, 2, 3, 4], 'obj': {'name': '娇娇'}})
    return result
